# Edge Human YOLO11n Pi 5

A lightweight YOLO11n human detection model for Raspberry Pi 5 and edge AI devices. Designed for developers who need a ready-to-run human detector without training from scratch.

<p align="center">
  <a href="#detailed-clone-and-usage-guide">Usage Guide</a> |
  <a href="#model-files">Model Files</a> |
  <a href="docs/MODEL_CARD.md">Model Card</a> |
  <a href="docs/DATASET_STATEMENT.md">Dataset Statement</a>
</p>

<p align="center">
  <a href="#detailed-clone-and-usage-guide">
    <img alt="Docs" src="https://img.shields.io/badge/DOCS-README-555555?style=for-the-badge">
  </a>
  <a href="https://github.com/Deron-Delivery-Drone/edge-human-yolo11n-pi5">
    <img alt="GitHub repository" src="https://img.shields.io/badge/GITHUB-EDGE--HUMAN--YOLO11N--PI5-facc15?style=for-the-badge">
  </a>
  <a href="models/README.md">
    <img alt="Model" src="https://img.shields.io/badge/MODEL-YOLO11N-4f46e5?style=for-the-badge">
  </a>
  <a href="LICENSE">
    <img alt="License AGPL-3.0" src="https://img.shields.io/badge/LICENSE-AGPL--3.0-2ea043?style=for-the-badge">
  </a>
  <a href="#raspberry-pi-5-notes">
    <img alt="Raspberry Pi 5 CPU only" src="https://img.shields.io/badge/PI%205-CPU--ONLY-ef4444?style=for-the-badge">
  </a>
  <a href="https://deron.vn">
    <img alt="Built by Deron" src="https://img.shields.io/badge/BUILT%20BY-DERON-8a2be2?style=for-the-badge">
  </a>
</p>

<p align="center">
  <a href="#english">
    <img alt="Language English" src="https://img.shields.io/badge/LANG-ENGLISH-555555?style=for-the-badge">
  </a>
  <a href="#tiếng-việt">
    <img alt="Language Vietnamese" src="https://img.shields.io/badge/LANG-TI%E1%BA%BENG%20VI%E1%BB%86T-16a34a?style=for-the-badge">
  </a>
  <a href="#中文">
    <img alt="Language Chinese" src="https://img.shields.io/badge/LANG-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge">
  </a>
</p>

## Features

- Human/person detection
- Raspberry Pi 5 target
- CPU-only inference
- No Hailo accelerator required
- YOLO11n-based lightweight model
- ONNX export support
- Image, video, and camera inference scripts
- Suitable for research, robotics, UAV, smart camera, and edge AI experiments

## Detailed Clone And Usage Guide

### English

#### 1. Prepare The Device

On Raspberry Pi 5 or Linux, install basic Python/OpenCV system dependencies:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv libgl1 libglib2.0-0
```

Raspberry Pi OS 64-bit is recommended. A stable power supply and cooling are also recommended because CPU temperature can affect inference speed.

#### 2. Clone The Repository

Open a terminal and run:

```bash
git clone https://github.com/Deron-Delivery-Drone/edge-human-yolo11n-pi5.git
cd edge-human-yolo11n-pi5
```

You should now see files such as `README.md`, `requirements.txt`, `run_image.py`, `run_video.py`, `run_camera.py`, and the `models/` directory.

#### 3. Create A Python Virtual Environment

On Raspberry Pi, Linux, or macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows PowerShell:

```powershell
py -3 -m venv venv
.\venv\Scripts\Activate.ps1
```

#### 4. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If OpenCV is difficult to install on Raspberry Pi, try installing the system OpenCV packages with apt or replace `opencv-python` with a headless OpenCV wheel suitable for your Raspberry Pi OS image.

#### 5. Verify The Model Files

The repository includes:

- `models/best.onnx` - recommended for Raspberry Pi CPU inference
- `models/best.pt` - PyTorch/Ultralytics checkpoint
- `models/SHA256SUMS` - checksums for model verification

Optional checksum verification on Linux/Raspberry Pi:

```bash
sha256sum -c models/SHA256SUMS
```

#### 6. Run Image Inference

Put your own test image in `samples/`, for example:

```text
samples/test.jpg
```

Then run:

```bash
python run_image.py --model models/best.onnx --source samples/test.jpg
```

Add `--save` if you want Ultralytics to save an annotated result:

```bash
python run_image.py --model models/best.onnx --source samples/test.jpg --save
```

The script prints detected people with confidence scores and bounding box coordinates.

#### 7. Run Video Inference

Place a test video in the project folder or pass an absolute path:

```bash
python run_video.py --model models/best.onnx --source input.mp4
```

Optional custom output path:

```bash
python run_video.py --model models/best.onnx --source input.mp4 --output output.mp4
```

The script writes an annotated video and prints simple FPS/latency statistics.

#### 8. Run Camera Inference

For a USB camera or Raspberry Pi camera exposed as an OpenCV camera index:

```bash
python run_camera.py --model models/best.onnx --camera 0
```

Press `q` to quit the display window.

For Raspberry Pi OS Lite or a headless SSH session:

```bash
python run_camera.py --model models/best.onnx --camera 0 --no-display
```

#### 9. Useful Options

- `--conf 0.25` changes the confidence threshold.
- `--imgsz 640` changes inference image size.
- `--device cpu` keeps inference on CPU.
- Use `models/best.onnx` for lightweight CPU deployment.
- Use `models/best.pt` if you specifically want PyTorch/Ultralytics inference.

Example:

```bash
python run_image.py --model models/best.onnx --source samples/test.jpg --conf 0.20 --imgsz 640
```

### Tiếng Việt

#### 1. Chuẩn Bị Thiết Bị

Trên Raspberry Pi 5 hoặc Linux, cài các gói hệ thống cơ bản cho Python/OpenCV:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv libgl1 libglib2.0-0
```

Khuyến nghị dùng Raspberry Pi OS 64-bit. Nên dùng nguồn ổn định và tản nhiệt tốt vì nhiệt độ CPU có thể ảnh hưởng trực tiếp đến tốc độ xử lý dữ liệu.

#### 2. Clone Repository Về Máy

Mở terminal và chạy:

```bash
git clone https://github.com/Deron-Delivery-Drone/edge-human-yolo11n-pi5.git
cd edge-human-yolo11n-pi5
```

Sau khi clone xong, bạn sẽ thấy các file như `README.md`, `requirements.txt`, `run_image.py`, `run_video.py`, `run_camera.py` và thư mục `models/`.

#### 3. Tạo Môi Trường Python Riêng

Trên Raspberry Pi, Linux hoặc macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Trên Windows PowerShell:

```powershell
py -3 -m venv venv
.\venv\Scripts\Activate.ps1
```

#### 4. Cài Thư Viện

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Nếu Raspberry Pi gặp lỗi khi cài OpenCV, hãy thử cài OpenCV bằng apt hoặc đổi `opencv-python` sang bản OpenCV headless phù hợp với Raspberry Pi OS của bạn.

#### 5. Kiểm Tra File Model

Repository đã có sẵn:

- `models/best.onnx` - khuyến nghị dùng trên Raspberry Pi CPU
- `models/best.pt` - checkpoint PyTorch/Ultralytics
- `models/SHA256SUMS` - checksum để kiểm tra model

Kiểm tra checksum trên Linux/Raspberry Pi nếu muốn:

```bash
sha256sum -c models/SHA256SUMS
```

#### 6. Chạy Nhận Diện Trên Ảnh

Đặt ảnh test của bạn vào thư mục `samples/`, ví dụ:

```text
samples/test.jpg
```

Sau đó chạy:

```bash
python run_image.py --model models/best.onnx --source samples/test.jpg
```

Thêm `--save` nếu muốn lưu ảnh kết quả có vẽ bounding box:

```bash
python run_image.py --model models/best.onnx --source samples/test.jpg --save
```

Script sẽ in ra người được phát hiện, confidence score và tọa độ bounding box.

#### 7. Chạy Nhận Diện Trên Video

Đặt video test trong thư mục project hoặc truyền đường dẫn tuyệt đối:

```bash
python run_video.py --model models/best.onnx --source input.mp4
```

Nếu muốn chỉ định file output:

```bash
python run_video.py --model models/best.onnx --source input.mp4 --output output.mp4
```

Script sẽ xuất video đã vẽ bounding box và in thống kê FPS/latency cơ bản.

#### 8. Chạy Nhận Diện Từ Camera

Với USB camera hoặc camera Raspberry Pi được OpenCV nhận thành camera index:

```bash
python run_camera.py --model models/best.onnx --camera 0
```

Nhấn `q` để thoát cửa sổ hiển thị.

Nếu chạy Raspberry Pi OS Lite hoặc SSH không có màn hình:

```bash
python run_camera.py --model models/best.onnx --camera 0 --no-display
```

#### 9. Một Số Tùy Chọn Hữu Ích

- `--conf 0.25` đổi ngưỡng confidence.
- `--imgsz 640` đổi kích thước ảnh inference.
- `--device cpu` ép chạy bằng CPU.
- Nên dùng `models/best.onnx` cho Raspberry Pi CPU.
- Dùng `models/best.pt` nếu bạn muốn chạy qua PyTorch/Ultralytics.

Ví dụ:

```bash
python run_image.py --model models/best.onnx --source samples/test.jpg --conf 0.20 --imgsz 640
```

### 中文

#### 1. 准备设备

在 Raspberry Pi 5 或 Linux 上，先安装 Python/OpenCV 所需的基础系统依赖：

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv libgl1 libglib2.0-0
```

建议使用 64 位 Raspberry Pi OS。为了获得更稳定的速度，也建议使用稳定电源和散热，因为 CPU 温度会影响推理性能。

#### 2. 克隆仓库

打开终端并运行：

```bash
git clone https://github.com/Deron-Delivery-Drone/edge-human-yolo11n-pi5.git
cd edge-human-yolo11n-pi5
```

克隆完成后，你应该能看到 `README.md`、`requirements.txt`、`run_image.py`、`run_video.py`、`run_camera.py` 以及 `models/` 目录。

#### 3. 创建 Python 虚拟环境

在 Raspberry Pi、Linux 或 macOS 上：

```bash
python3 -m venv venv
source venv/bin/activate
```

在 Windows PowerShell 上：

```powershell
py -3 -m venv venv
.\venv\Scripts\Activate.ps1
```

#### 4. 安装依赖

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

如果在 Raspberry Pi 上安装 OpenCV 遇到问题，可以尝试使用 apt 安装系统 OpenCV 包，或把 `opencv-python` 换成适合你的 Raspberry Pi OS 镜像的 headless OpenCV wheel。

#### 5. 检查模型文件

本仓库已包含：

- `models/best.onnx` - 推荐用于 Raspberry Pi CPU 推理
- `models/best.pt` - PyTorch/Ultralytics checkpoint
- `models/SHA256SUMS` - 用于校验模型文件的 checksum

在 Linux/Raspberry Pi 上可以选择运行：

```bash
sha256sum -c models/SHA256SUMS
```

#### 6. 对图片运行推理

把你自己的测试图片放到 `samples/` 目录，例如：

```text
samples/test.jpg
```

然后运行：

```bash
python run_image.py --model models/best.onnx --source samples/test.jpg
```

如果想保存带检测框的结果图片，添加 `--save`：

```bash
python run_image.py --model models/best.onnx --source samples/test.jpg --save
```

脚本会输出检测到的人、置信度以及 bounding box 坐标。

#### 7. 对视频运行推理

把测试视频放在项目目录，或传入绝对路径：

```bash
python run_video.py --model models/best.onnx --source input.mp4
```

指定输出文件：

```bash
python run_video.py --model models/best.onnx --source input.mp4 --output output.mp4
```

脚本会生成带检测框的视频，并输出简单的 FPS/latency 统计。

#### 8. 使用摄像头运行推理

如果 USB 摄像头或 Raspberry Pi 摄像头可以被 OpenCV 识别为 camera index：

```bash
python run_camera.py --model models/best.onnx --camera 0
```

按 `q` 退出显示窗口。

如果使用 Raspberry Pi OS Lite 或通过 SSH 在无显示环境运行：

```bash
python run_camera.py --model models/best.onnx --camera 0 --no-display
```

#### 9. 常用参数

- `--conf 0.25` 修改置信度阈值。
- `--imgsz 640` 修改推理输入尺寸。
- `--device cpu` 强制使用 CPU。
- 推荐使用 `models/best.onnx` 进行 Raspberry Pi CPU 部署。
- 如果需要 PyTorch/Ultralytics 推理，可以使用 `models/best.pt`。

示例：

```bash
python run_image.py --model models/best.onnx --source samples/test.jpg --conf 0.20 --imgsz 640
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
