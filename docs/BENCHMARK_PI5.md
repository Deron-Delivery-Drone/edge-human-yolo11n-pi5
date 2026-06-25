# Raspberry Pi 5 Benchmark Template

No official Raspberry Pi 5 benchmark numbers are published for this release yet. Use this table to record measured results from your own hardware.

| Device | Model format | Image size | Backend | FPS | Latency | CPU usage | Notes |
|---|---|---:|---|---:|---:|---:|---|
| TODO: Raspberry Pi 5 8 GB | `best.onnx` | 640 | ONNX Runtime CPU | TODO | TODO | TODO | Measure with `run_video.py` or your camera pipeline |
| TODO: Raspberry Pi 5 8 GB | `best.pt` | 640 | PyTorch CPU via Ultralytics | TODO | TODO | TODO | Compare against ONNX |
| TODO: Raspberry Pi 5 8 GB | `best.onnx` | 480 | ONNX Runtime CPU | TODO | TODO | TODO | Optional lower-latency test |

## Benchmark Notes

- Use Raspberry Pi OS 64-bit when possible.
- Record CPU temperature and throttling state during longer runs.
- Keep camera resolution, image size, confidence threshold, and backend fixed when comparing runs.
- Do not report estimated values as measured results.
