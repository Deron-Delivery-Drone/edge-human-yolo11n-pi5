# Edge Human YOLO11n Pi 5

A lightweight YOLO11n human detection model for Raspberry Pi 5 and edge AI devices. Designed for developers who need a ready-to-run human detector without training from scratch.

## Features

- Human/person detection
- Raspberry Pi 5 target
- CPU-only inference
- No Hailo accelerator required
- YOLO11n-based lightweight model
- ONNX export support
- Image, video, and camera inference scripts
- Suitable for research, robotics, UAV, smart camera, and edge AI experiments

## Quick Start

```bash
git clone https://github.com/Deron-Delivery-Drone/edge-human-yolo11n-pi5.git
cd edge-human-yolo11n-pi5

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

Run inference on an image:

```bash
python run_image.py --model models/best.onnx --source samples/test.jpg
```

Run inference on a video:

```bash
python run_video.py --model models/best.onnx --source input.mp4
```

Run inference from a camera:

```bash
python run_camera.py --model models/best.onnx --camera 0
```

## Model Files

This release includes:

- `models/best.pt` - YOLO11n PyTorch checkpoint
- `models/best.onnx` - ONNX export for edge deployment

The model is a single-class human/person detector. The class list is available in `export/classes.txt`, and a minimal YOLO data file is available in `export/data.yaml`.

If future model files become too large for normal git history, they should be distributed through GitHub Releases instead of being committed directly.

## Raspberry Pi 5 Notes

Raspberry Pi OS 64-bit is recommended. ONNX may be preferable for deployment on Raspberry Pi 5 CPU because it can run through ONNX Runtime without requiring PyTorch at inference time.

Actual FPS depends on image size, camera, CPU temperature, power supply, thermal throttling, operating system image, and inference backend. No Hailo accelerator is required for the provided scripts.

On Raspberry Pi OS Lite or other headless environments, use `run_camera.py --no-display` or run video/image inference instead of opening a GUI window.

If `opencv-python` is difficult to install on Raspberry Pi, try the system OpenCV package from apt or use a headless OpenCV wheel appropriate for your image.

## Dataset Notice

The original training dataset is not redistributed.

The model was trained using mixed manually labeled and web-collected images for research/prototyping. The individual rights/licenses of every original image have not been fully verified. Users should not assume the dataset is commercially cleared.

This repository shares only the trained model files, inference scripts, and documentation. It does not include raw training images, scraped web images, labels, dataset manifests, or private DeronAI development code.

## Intended Use

- Research
- Education
- Edge AI testing
- Robotics prototypes
- Raspberry Pi AI benchmarking
- UAV and smart camera experiments

## Not Intended For

- Biometric identification
- Face recognition
- Tracking specific people
- Production surveillance without review
- Law enforcement deployment
- Safety-critical deployment
- Commercial deployment without license and dataset review

## License

This project is released under the GNU Affero General Public License v3.0 (AGPL-3.0). See `LICENSE`.

This model was trained using Ultralytics YOLO tooling. Users are responsible for checking Ultralytics YOLO licensing terms, AGPL-3.0 obligations, third-party dependency licenses, and dataset rights before production or commercial use.

## Disclaimer

This is a prototype model for research and educational edge AI experiments. Users are responsible for compliance with model licensing, dataset rights, privacy rules, and local laws.
