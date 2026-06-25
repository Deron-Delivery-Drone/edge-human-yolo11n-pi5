from __future__ import annotations

import argparse
from pathlib import Path

from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run YOLO11n human detection on one image.")
    parser.add_argument("--model", required=True, help="Path to .pt or .onnx model.")
    parser.add_argument("--source", required=True, help="Path to input image.")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold.")
    parser.add_argument("--imgsz", type=int, default=640, help="Inference image size.")
    parser.add_argument("--device", default="cpu", help="Inference device, default: cpu.")
    parser.add_argument("--save", action="store_true", help="Save annotated result through Ultralytics.")
    return parser.parse_args()


def print_detections(result) -> None:
    boxes = result.boxes
    if boxes is None or len(boxes) == 0:
        print("No detections.")
        return

    names = result.names
    for index, box in enumerate(boxes, start=1):
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        xyxy = [float(value) for value in box.xyxy[0]]
        label = names.get(cls_id, str(cls_id))
        print(
            f"{index}: {label} conf={conf:.3f} "
            f"xyxy=({xyxy[0]:.1f}, {xyxy[1]:.1f}, {xyxy[2]:.1f}, {xyxy[3]:.1f})"
        )


def main() -> int:
    args = parse_args()
    source = Path(args.source)
    if not source.exists():
        raise FileNotFoundError(f"Input image not found: {source}")

    model = YOLO(args.model)
    results = model.predict(
        source=str(source),
        conf=args.conf,
        imgsz=args.imgsz,
        device=args.device,
        save=args.save,
        verbose=False,
    )

    for result in results:
        print(f"Source: {result.path}")
        print_detections(result)
        save_dir = getattr(result, "save_dir", None)
        if args.save and save_dir:
            print(f"Saved annotated output to: {save_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
