from __future__ import annotations

import argparse
import time
from pathlib import Path

import cv2
from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run YOLO11n human detection on a video.")
    parser.add_argument("--model", required=True, help="Path to .pt or .onnx model.")
    parser.add_argument("--source", required=True, help="Path to input video.")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold.")
    parser.add_argument("--imgsz", type=int, default=640, help="Inference image size.")
    parser.add_argument("--output", default="output.mp4", help="Path for annotated output video.")
    parser.add_argument("--device", default="cpu", help="Inference device, default: cpu.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = Path(args.source)
    if not source.exists():
        raise FileNotFoundError(f"Input video not found: {source}")

    cap = cv2.VideoCapture(str(source))
    if not cap.isOpened():
        raise RuntimeError(f"Could not open video: {source}")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    input_fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    writer = cv2.VideoWriter(
        args.output,
        cv2.VideoWriter_fourcc(*"mp4v"),
        input_fps,
        (width, height),
    )
    if not writer.isOpened():
        cap.release()
        raise RuntimeError(f"Could not open output video: {args.output}")

    model = YOLO(args.model)
    frame_count = 0
    infer_seconds = 0.0
    wall_start = time.perf_counter()

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            infer_start = time.perf_counter()
            result = model.predict(
                source=frame,
                conf=args.conf,
                imgsz=args.imgsz,
                device=args.device,
                verbose=False,
            )[0]
            infer_seconds += time.perf_counter() - infer_start

            annotated = result.plot()
            writer.write(annotated)
            frame_count += 1

            if frame_count % 30 == 0:
                avg_infer_ms = infer_seconds * 1000.0 / frame_count
                avg_fps = frame_count / max(time.perf_counter() - wall_start, 1e-9)
                print(f"frames={frame_count} avg_infer_ms={avg_infer_ms:.1f} avg_fps={avg_fps:.2f}")
    finally:
        cap.release()
        writer.release()

    wall_seconds = time.perf_counter() - wall_start
    avg_infer_ms = infer_seconds * 1000.0 / max(frame_count, 1)
    avg_fps = frame_count / max(wall_seconds, 1e-9)
    print(f"Processed {frame_count} frames")
    print(f"Average inference latency: {avg_infer_ms:.1f} ms/frame")
    print(f"Average end-to-end FPS: {avg_fps:.2f}")
    print(f"Saved annotated video to: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
