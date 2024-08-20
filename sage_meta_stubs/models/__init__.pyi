# Stub for sage_meta.models

from typing import Dict, List, Optional
from dataclasses import dataclass, field

@dataclass
class Category:
    id: str
    name: str

@dataclass
class Insight:
    id: str
    name: str
    period: str
    values: List[Dict[str, str]] = field(default_factory=list)
    title: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)

@dataclass
class AccountInsight:
    id: str
    name: str
    period: str
    values: List[Dict[str, str]] = field(default_factory=list)
    title: Optional[str] = field(default="")
    description: Optional[str] = field(default="")

@dataclass
class Comment:
    id: str
    text: Optional[str] = field(default=None)
    username: Optional[str] = field(default=None)
    like_count: Optional[int] = field(default=None)
    timestamp: Optional[str] = field(default=None)
    additional_data: Dict[str, Optional[str]] = field(default_factory=dict)

@dataclass
class Story:
    id: str
    media_type: Optional[str] = field(default=None)
    media_url: Optional[str] = field(default=None)
    timestamp: Optional[str] = field(default=None)
    additional_data: Dict[str, Optional[str]] = field(default_factory=dict)

@dataclass
class Media:
    id: str
    caption: Optional[str] = field(default=None)
    media_type: Optional[str] = field(default=None)
    media_url: List[str] = field(default_factory=list)
    timestamp: Optional[str] = field(default=None)
    like_count: Optional[int] = field(default=None)
    comments_count: Optional[int] = field(default=None)
    comments: List[Comment] = field(default_factory=list)
    additional_data: Dict[str, Optional[str]] = field(default_factory=dict)

@dataclass
class InstagramAccount:
    id: str
    username: str
    follows_count: int
    followers_count: int
    media_count: int
    profile_picture_url: Optional[str] = field(default=None)
    website: Optional[str] = field(default=None)
    biography: Optional[str] = field(default=None)
    media: List[Media] = field(default_factory=list)
    insights: List[Insight] = field(default_factory=list)
    stories: List[Story] = field(default_factory=list)
    additional_data: Dict[str, Optional[str]] = field(default_factory=dict)

@dataclass
class FacebookPageData:
    id: str
    name: str
    category: str
    access_token: str
    category_list: List[Category] = field(default_factory=list)
    tasks: List[str] = field(default_factory=list)
    instagram_business_account: Optional[InstagramAccount] = field(default=None)
    additional_data: Dict[str, Optional[str]] = field(default_factory=dict)

@dataclass
class UserData:
    id: str
    name: str
    email: Optional[str] = field(default=None)
    pages: List[FacebookPageData] = field(default_factory=list)
    additional_data: Dict[str, Optional[str]] = field(default_factory=dict)

@dataclass
class PostMention:
    id: str
    media_type: str
    media_url: str
    caption: str
    comments_count: int
    like_count: int
    timestamp: str
    username: str
    owner: str
    additional_data: Dict[str, Optional[str]] = field(default_factory=dict)

@dataclass
class CommentMention:
    id: str
    text: str
    like_count: int
    timestamp: str
    username: str
    additional_data: Dict[str, Optional[str]] = field(default_factory=dict)

@dataclass
class ReplyMention:
    id: str
    message: str
    timestamp: str
    additional_data: Dict[str, Optional[str]] = field(default_factory=dict)