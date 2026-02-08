---
ID: HM-CAT-003
Status: ACTIVE
Source: github.com/BigRigVibeCoder/HiveMind
---

# Component Specification: Luxonis OAK-D Lite

**Role:** Primary Vision & Depth Perception Unit\
**Architecture:** Edge AI Coprocessor (VPU)\
**Interface:** USB 3.0 (Type-C)\
**Data Protocol:** XLink (Serialized Data Packets)

## 1. Core Concept: "The Smart Eye"

The OAK-D Lite differs from a standard camera in that it processes raw visual data **on-device** using the Intel Movidius Myriad X VPU.

- **Input:** Raw image data from 3 onboard sensors.

- **Processing (On-Device):**

  - **Stereo Depth:** Calculates disparity between Left/Right cameras to generate a Z-depth map.

  - **Neural Inference:** Runs `.blob` models (YOLO, MobileNet) to detect objects.

  - **Spatial Calculation:** Combines Depth + AI to calculate the exact X, Y, Z metric coordinates of an object relative to the camera.

- **Output:** Lightweight Metadata packets (e.g., `"Cup detected at X:20cm, Y:5cm, Z:50cm"`).

**Engineering Implication:** The Host Computer (Odroid) does **zero** image processing. It simply receives a stream of coordinates, keeping the CPU free for LLM and Motion Control tasks.

## 2. Hardware Architecture

### 2.1 Sensors

- **RGB Camera (Center):** 13MP (Sony IMX214). Used for AI inference and color video streaming.

- **Stereo Cameras (Left/Right):** 640x480 (OmniVision OV7251). Global Shutter (excellent for robotics/motion). Used for depth calculation.

- **Focus Type:** **Fixed-Focus** (Selected for K9 to prevent vibration damage).

### 2.2 The Compute Engine (VPU)

- **Chip:** Intel Movidius Myriad X.

- **Performance:** 4 TOPS (Trillions of Operations Per Second).

- **Power Consumption:** 2.5W - 5W (Powered via USB-C).

## 3. Data Interface & Protocol

While physically connected via USB, the device does not act like a simple serial port (UART). It uses **XLink**, a high-speed protocol that wraps data streams.

### 3.1 The "Output Pipelines"

You can configure the camera to output multiple streams simultaneously.

1. **NN Output (Metadata - Very Low Bandwidth):**

   - **Payload:** Array of Detections.

   - **Structure:** `[Label_ID, Confidence, BoundingBox_Rect, Spatial_X, Spatial_Y, Spatial_Z]`.

   - **Usage:** Primary input for K9's "Brain" and "Reflex" layers.

2. **Depth Map (Video - Medium Bandwidth):**

   - **Payload:** 16-bit Grayscale Video.

   - **Usage:** Fed into ROS 2 `Nav2` for obstacle costmaps.

3. **RGB Video (Video - High Bandwidth):**

   - **Payload:** NV12 or MJPEG encoded video.

   - **Usage:** Streaming to the Operator's HUD (Foxglove Studio).

### 3.2 Example Data Packet (JSON Representation)

*What the Odroid receives when the camera sees a person:*

```
{
  "detections": [
    {
      "label": "person",
      "confidence": 0.98,
      "spatialCoordinates": {
        "x": 105.0,  // mm right of center
        "y": -50.0,  // mm below center
        "z": 1500.0  // mm distance (1.5 meters away)
      },
      "boundingBox": {
        "xmin": 0.4, "ymin": 0.2, "xmax": 0.6, "ymax": 0.8
      }
    }
  ]
}
```

## 4. ROS 2 Integration (`depthai_ros_driver`)

The OAK-D Lite has a native ROS 2 driver that handles the XLink communication and publishes standard ROS messages.

| ROS 2 Topic | Message Type | Description |
| --- | --- | --- |
| `/oak/nn/spatial_detections` | `depthai_ros_msgs/SpatialDetectionArray` | **The Critical Feed.** Contains the 3D coordinates of objects. |
| `/oak/rgb/image_raw` | `sensor_msgs/Image` | Visual video feed. |
| `/oak/stereo/image_raw` | `sensor_msgs/Image` | Depth heat map. |
| `/oak/points` | `sensor_msgs/PointCloud2` | Full 3D point cloud (Heavy bandwidth, use sparingly). |

## 5. Limitations & Constraints

1. **Minimum Depth:** \~20cm. Objects closer than this cannot be seen in 3D (Blind spot).

   - *Mitigation:* This is why we added the "Chin" sensor (ToF) for the K9.

2. **Low Light:** Passive stereo depth requires light. It fails in pitch blackness.

   - *Mitigation:* We added the "Sun" module (LEDs) or rely on LIDAR in the dark.

3. **USB Bandwidth:** Streaming 4K Video + Point Clouds requires USB 3.0.

   - *Constraint:* Ensure it is plugged into the **Blue** USB ports on the Odroid.

## 6. Summary for Engineers

The OAK-D Lite acts as a **Sensor-to-Object Gateway**.

- **Input:** Reality.

- **Output:** Coordinates (`XYZ`).

- **Load:** &lt; 5% CPU usage on the host computer.