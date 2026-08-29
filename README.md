# 나만의 프롬프트 관리 시스템


# 프롬프트 데이터 구조: 제목, 내용, 카테고리, 즐겨찾기 여부
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 밝고 현대적인 스타일로 제작해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "뉴스 요약 프롬프트",
        "content": "주어진 뉴스 기사를 3줄로 요약해주세요. 가장 중요한 정보를 먼저 배치하세요.",
        "category": "자동화",
        "favorite": False
    }
]

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

# 메인 메뉴
def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")
    choice = input("선택: ")
    return choice

# 프롬프트 추가
def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    title = input("제목: ").strip()
    if not title:
        print("제목을 입력해주세요.")
        return
    
    content = input("내용: ").strip()
    if not content:
        print("내용을 입력해주세요.")
        return
    
    print("\n카테고리 선택:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")
    cat_choice = input("선택: ").strip()
    
    if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(CATEGORIES):
        category = CATEGORIES[int(cat_choice) - 1]
    else:
        category = cat_choice if cat_choice else "기타"
    
    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })
    print("✅ 프롬프트가 추가되었습니다!")

# 프롬프트 목록
def show_list():
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    
    for i, p in enumerate(prompts, 1):
        star = "⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']} {star}")
    print(f"\n총 {len(prompts)}개의 프롬프트")

# 카테고리별 조회
def view_by_category():
    print("\n=== 카테고리별 조회 ===")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")
    cat_choice = input("선택: ").strip()
    
    if not cat_choice.isdigit() or not (1 <= int(cat_choice) <= len(CATEGORIES)):
        print("올바른 번호를 입력해주세요.")
        return
    
    selected_category = CATEGORIES[int(cat_choice) - 1]
    filtered = [p for p in prompts if p["category"] == selected_category]
    
    print(f"\n[{selected_category}] 카테고리 프롬프트:")
    if not filtered:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return
    
    for i, p in enumerate(filtered, 1):
        star = "⭐" if p["favorite"] else ""
        print(f"{i}. {p['title']} {star}")
    print(f"\n총 {len(filtered)}개의 프롬프트")

# 프롬프트 검색
def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어: ").strip()
    
    if not keyword:
        print("검색어를 입력해주세요.")
        return
    
    results = [p for p in prompts if keyword in p["title"] or keyword in p["content"]]
    
    print("\n검색 결과:")
    if not results:
        print("검색 결과가 없습니다.")
        return
    
    for i, p in enumerate(results, 1):
        star = "⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']} {star}")
    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")

# 프롬프트 상세 보기
def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")
    try:
        num = int(input("번호 입력: ").strip())
        if 1 <= num <= len(prompts):
            p = prompts[num - 1]
            star = "⭐" if p["favorite"] else "☆"
            print("\n" + "─" * 40)
            print(f"제목: {p['title']}")
            print(f"카테고리: {p['category']}")
            print(f"즐겨찾기: {star}")
            print("─" * 40)
            print(f"내용:\n{p['content']}")
            print("─" * 40)
        else:
            print("올바른 번호를 입력해주세요.")
    except ValueError:
        print("숫자를 입력해주세요.")

# 즐겨찾기 관리
def toggle_favorite():
    print("\n=== 즐겨찾기 관리 ===")
    try:
        num = int(input("프롬프트 번호 입력: ").strip())
        if 1 <= num <= len(prompts):
            p = prompts[num - 1]
            p["favorite"] = not p["favorite"]
            status = "추가했습니다!" if p["favorite"] else "제거했습니다!"
            print(f"✅ '{p['title']}' 프롬프트를 즐겨찾기에 {status}")
        else:
            print("올바른 번호를 입력해주세요.")
    except ValueError:
        print("숫자를 입력해주세요.")

# 즐겨찾기 목록
def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")
    favorites = [p for p in prompts if p["favorite"]]
    
    if not favorites:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return
    
    for i, p in enumerate(favorites, 1):
        print(f"{i}. [{p['category']}] {p['title']} ⭐")
    print(f"\n총 {len(favorites)}개의 즐겨찾기")

# 메인 프로그램
def main():
    while True:
        choice = show_menu()
        
        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            view_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "0":
            print("\n👋 프로그램을 종료합니다.")
            break
        else:
            print("❌ 올바른 번호를 입력해주세요.")

if __name__ == "__main__":
    main()
