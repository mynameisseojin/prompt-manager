from constants import CATEGORIES, DEFAULT_PROMPTS
from copy import deepcopy


class PromptManager:
    """프롬프트 데이터를 관리하는 클래스"""
    
    def __init__(self):
        # 기본 프롬프트로 초기화
        self.prompts = deepcopy(DEFAULT_PROMPTS)
    
    def add_prompt(self, title, content, category):
        """새 프롬프트 추가"""
        new_prompt = {
            "title": title,
            "content": content,
            "category": category,
            "favorite": False
        }
        self.prompts.append(new_prompt)
        return True
    
    def get_all_prompts(self):
        """모든 프롬프트 반환"""
        return self.prompts
    
    def get_prompts_by_category(self, category):
        """카테고리별 프롬프트 반환"""
        return [p for p in self.prompts if p["category"] == category]
    
    def search_prompts(self, keyword):
        """프롬프트 검색 (제목 또는 내용)"""
        keyword = keyword.lower()
        results = []
        for prompt in self.prompts:
            if (keyword in prompt["title"].lower() or 
                keyword in prompt["content"].lower()):
                results.append(prompt)
        return results
    
    def search_by_title(self, title_keyword):
        """제목으로만 검색"""
        keyword = title_keyword.lower()
        return [p for p in self.prompts if keyword in p["title"].lower()]
    
    def search_by_content(self, content_keyword):
        """내용으로만 검색"""
        keyword = content_keyword.lower()
        return [p for p in self.prompts if keyword in p["content"].lower()]
    
    def search_by_category_and_keyword(self, category, keyword):
        """카테고리와 키워드로 동시에 검색"""
        category_prompts = self.get_prompts_by_category(category)
        keyword = keyword.lower()
        return [p for p in category_prompts 
                if keyword in p["title"].lower() or keyword in p["content"].lower()]
    
    def get_prompt_by_index(self, index):
        """인덱스로 프롬프트 조회"""
        if 0 <= index < len(self.prompts):
            return self.prompts[index]
        return None
    
    def toggle_favorite(self, index):
        """즐겨찾기 토글"""
        if 0 <= index < len(self.prompts):
            self.prompts[index]["favorite"] = not self.prompts[index]["favorite"]
            return self.prompts[index]["favorite"]
        return None
    
    def get_favorites(self):
        """즐겨찾기 목록 반환"""
        return [p for p in self.prompts if p["favorite"]]
    
    def get_prompt_count(self):
        """전체 프롬프트 개수"""
        return len(self.prompts)
    
    def get_favorite_count(self):
        """즐겨찾기 개수"""
        return len(self.get_favorites())
    
    def get_category_count(self, category):
        """카테고리별 프롬프트 개수"""
        return len(self.get_prompts_by_category(category))
    
    def is_favorite(self, index):
        """특정 프롬프트의 즐겨찾기 여부 확인"""
        prompt = self.get_prompt_by_index(index)
        return prompt['favorite'] if prompt else False