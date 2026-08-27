#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
프롬프트 관리 시스템 기능 테스트
"""

from prompt_manager import PromptManager
from constants import CATEGORIES


def test_basic_functionality():
    """기본 기능 테스트"""
    print("=" * 50)
    print("프롬프트 관리 시스템 테스트")
    print("=" * 50)
    
    # 1. 관리자 초기화
    manager = PromptManager()
    print(f"\n✅ 관리자 초기화 성공")
    print(f"   기본 프롬프트: {manager.get_prompt_count()}개 로드됨")
    
    # 2. 모든 프롬프트 조회
    print(f"\n✅ 모든 프롬프트 조회")
    prompts = manager.get_all_prompts()
    for i, prompt in enumerate(prompts, 1):
        print(f"   {i}. {prompt['title']} - {prompt['category']}")
    
    # 3. 프롬프트 추가
    print(f"\n✅ 프롬프트 추가")
    manager.add_prompt(
        "이메일 작성 도우미",
        "전문적이고 친근한 톤의 이메일을 작성해주세요.",
        "텍스트 생성"
    )
    print(f"   현재 프롬프트: {manager.get_prompt_count()}개")
    
    # 4. 카테고리별 검색
    print(f"\n✅ 카테고리별 검색")
    text_prompts = manager.get_prompts_by_category("텍스트 생성")
    print(f"   '텍스트 생성' 카테고리: {len(text_prompts)}개")
    for p in text_prompts:
        print(f"   - {p['title']}")
    
    # 5. 키워드 검색
    print(f"\n✅ 키워드 검색")
    search_result = manager.search_prompts("블로그")
    print(f"   '블로그' 검색 결과: {len(search_result)}개")
    for p in search_result:
        print(f"   - {p['title']}")
    
    # 6. 즐겨찾기 기능
    print(f"\n✅ 즐겨찾기 기능")
    manager.toggle_favorite(0)
    print(f"   0번 프롬프트 즐겨찾기 추가")
    
    favorites = manager.get_favorites()
    print(f"   총 즐겨찾기: {len(favorites)}개")
    for p in favorites:
        print(f"   ⭐ {p['title']}")
    
    # 7. 프롬프트 상세 조회
    print(f"\n✅ 프롬프트 상세 조회")
    prompt = manager.get_prompt_by_index(0)
    if prompt:
        print(f"   제목: {prompt['title']}")
        print(f"   카테고리: {prompt['category']}")
        print(f"   즐겨찾기: {'⭐ Yes' if prompt['favorite'] else '☆ No'}")
        print(f"   내용: {prompt['content'][:50]}...")
    
    # 8. 유틸리티 메서드
    print(f"\n✅ 유틸리티 메서드")
    print(f"   전체 프롬프트: {manager.get_prompt_count()}개")
    print(f"   즐겨찾기: {manager.get_favorite_count()}개")
    print(f"   텍스트 생성 카테고리: {manager.get_category_count('텍스트 생성')}개")
    
    print("\n" + "=" * 50)
    print("✅ 모든 테스트 완료!")
    print("=" * 50)


if __name__ == "__main__":
    test_basic_functionality()