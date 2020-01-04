from dataclasses import dataclass
from typing import Optional, Dict, Any

from dacite import from_dict


@dataclass(frozen=True)
class Profile:
    avatar_hash: str
    status_text: str
    status_emoji: str
    status_expiration: int
    real_name: str
    display_name: str
    real_name_normalized: str
    display_name_normalized: str
    image_24: str
    image_32: str
    image_48: str
    image_72: str
    image_192: str
    image_512: str
    team: str
    email: Optional[str] = None
    image_original: Optional[str] = None


@dataclass(frozen=True)
class User:
    """
    User model that represents a user object from the Slack API
    """
    id: str
    team_id: str
    name: str
    deleted: bool
    profile: Profile
    is_bot: bool
    updated: int
    is_app_user: bool
    color: Optional[str] = None
    real_name: Optional[str] = None
    tz: Optional[str] = None
    tz_label: Optional[str] = None
    tz_offset: Optional[int] = None
    is_admin: Optional[bool] = None
    is_owner: Optional[bool] = None
    is_primary_owner: Optional[bool] = None
    is_restricted: Optional[bool] = None
    is_ultra_restricted: Optional[bool] = None
    is_stranger: Optional[bool] = None
    has_2fa: Optional[bool] = None
    locale: Optional[str] = None

    @staticmethod
    def from_api_response(user_reponse: Dict[str, Any]) -> 'User':
        return from_dict(data_class=User, data=user_reponse)  # pragma: no cover

    def fmt_mention(self) -> str:
        return "<@{}>".format(self.id)
