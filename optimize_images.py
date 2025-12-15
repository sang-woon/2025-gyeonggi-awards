from PIL import Image
import os

# 설정
INPUT_DIR = "images"
OUTPUT_DIR = "images/optimized"
MAX_WIDTH = 800
MAX_HEIGHT = 1200
QUALITY = 85

# 출력 디렉토리 생성
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 최적화할 이미지 목록
images_to_optimize = [
    "간부공무원-정두석.png",
    "간부공무원-허승범.png",
    "간부공무원-박래혁.png",
    "간부공무원-배진기.png",
    "간부공무원-김영옥.png",
    "도의원-이제영.jpg",
    "도의원-임창휘.png",
    "도의원-윤성근.jpg",
    "도의원-장민수.jpg",
    "도의원-김성남.png",
]

for filename in images_to_optimize:
    input_path = os.path.join(INPUT_DIR, filename)
    
    if not os.path.exists(input_path):
        print(f"파일 없음: {filename}")
        continue
    
    try:
        with Image.open(input_path) as img:
            # RGBA를 RGB로 변환 (JPEG 저장을 위해)
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # 비율 유지하며 리사이즈
            ratio = min(MAX_WIDTH / img.width, MAX_HEIGHT / img.height)
            if ratio < 1:
                new_size = (int(img.width * ratio), int(img.height * ratio))
                img = img.resize(new_size, Image.Resampling.LANCZOS)
            
            # 출력 파일명 (모두 jpg로 통일)
            output_filename = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            
            # 저장
            img.save(output_path, "JPEG", quality=QUALITY, optimize=True)
            
            # 파일 크기 비교
            original_size = os.path.getsize(input_path) / 1024 / 1024
            optimized_size = os.path.getsize(output_path) / 1024 / 1024
            
            print(f"✓ {filename}")
            print(f"  원본: {original_size:.2f}MB → 최적화: {optimized_size:.2f}MB ({img.width}x{img.height})")
            
    except Exception as e:
        print(f"오류 ({filename}): {e}")

print("\n완료! 최적화된 이미지가 images/optimized/ 폴더에 저장되었습니다.")

