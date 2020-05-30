#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © Nekoka.tt 2019-2020
#
# This file is part of Hikari.
#
# Hikari is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hikari is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Hikari. If not, see <https://www.gnu.org/licenses/>.
"""Application and entities that are used to describe guilds on Discord."""

from __future__ import annotations

__all__ = [
    "ActivityAssets",
    "ActivityFlag",
    "ActivitySecret",
    "ActivityTimestamps",
    "ActivityType",
    "ActivityParty",
    "ClientStatus",
    "Guild",
    "GuildWidget",
    "Role",
    "GuildFeature",
    "GuildSystemChannelFlag",
    "GuildMessageNotificationsLevel",
    "GuildExplicitContentFilterLevel",
    "GuildMFALevel",
    "GuildVerificationLevel",
    "GuildPremiumTier",
    "GuildPreview",
    "GuildMember",
    "GuildMemberPresence",
    "Integration",
    "GuildMemberBan",
    "IntegrationAccount",
    "IntegrationExpireBehaviour",
    "PartialGuild",
    "PartialIntegration",
    "PartialRole",
    "PresenceActivity",
    "PresenceStatus",
    "PresenceUser",
    "UnavailableGuild",
]

import enum
import typing

import attr

from hikari.models import bases
from hikari.models import users
from hikari.net import urls
from hikari.utilities import undefined

if typing.TYPE_CHECKING:
    import datetime

    from hikari.models import channels as channels_
    from hikari.models import colors
    from hikari.models import emojis as emojis_
    from hikari.models import permissions as permissions_


@enum.unique
class GuildExplicitContentFilterLevel(int, enum.Enum):
    """Represents the explicit content filter setting for a guild."""

    DISABLED = 0
    """No explicit content filter."""

    MEMBERS_WITHOUT_ROLES = 1
    """Filter posts from anyone without a role."""

    ALL_MEMBERS = 2
    """Filter all posts."""


@enum.unique
class GuildFeature(str, enum.Enum):
    """Features that a guild can provide."""

    ANIMATED_ICON = "ANIMATED_ICON"
    """Guild has access to set an animated guild icon."""

    BANNER = "BANNER"
    """Guild has access to set a guild banner image."""

    COMMERCE = "COMMERCE"
    """Guild has access to use commerce features (i.e. create store channels)."""

    DISCOVERABLE = "DISCOVERABLE"
    """Guild is able to be discovered in the directory."""

    FEATURABLE = "FEATURABLE"
    """Guild is able to be featured in the directory."""

    INVITE_SPLASH = "INVITE_SPLASH"
    """Guild has access to set an invite splash background."""

    MORE_EMOJI = "MORE_EMOJI"
    """More emojis can be hosted in this guild than normal."""

    NEWS = "NEWS"
    """Guild has access to create news channels."""

    LURKABLE = "LURKABLE"
    """People can view channels in this guild without joining."""

    PARTNERED = "PARTNERED"
    """Guild is partnered."""

    PUBLIC = "PUBLIC"
    """Guild is public, go figure."""

    PUBLIC_DISABLED = "PUBLIC_DISABLED"
    """Guild cannot be public. Who would have guessed?"""

    VANITY_URL = "VANITY_URL"
    """Guild has access to set a vanity URL."""

    VERIFIED = "VERIFIED"
    """Guild is verified."""

    VIP_REGIONS = "VIP_REGIONS"
    """Guild has access to set 384kbps bitrate in voice.

    Previously gave access to VIP voice servers.
    """

    WELCOME_SCREEN_ENABLED = "WELCOME_SCREEN_ENABLED"
    """Guild has enabled the welcome screen."""


@enum.unique
class GuildMessageNotificationsLevel(int, enum.Enum):
    """Represents the default notification level for new messages in a guild."""

    ALL_MESSAGES = 0
    """Notify users when any message is sent."""

    ONLY_MENTIONS = 1
    """Only notify users when they are @mentioned."""


@enum.unique
class GuildMFALevel(int, enum.Enum):
    """Represents the multi-factor authorization requirement for a guild."""

    NONE = 0
    """No MFA requirement."""

    ELEVATED = 1
    """MFA requirement."""


@enum.unique
class GuildPremiumTier(int, enum.Enum):
    """Tier for Discord Nitro boosting in a guild."""

    NONE = 0
    """No Nitro boost level."""

    TIER_1 = 1
    """Level 1 Nitro boost."""

    TIER_2 = 2
    """Level 2 Nitro boost."""

    TIER_3 = 3
    """Level 3 Nitro boost."""


@enum.unique
class GuildSystemChannelFlag(enum.IntFlag):
    """Defines which features are suppressed in the system channel."""

    SUPPRESS_USER_JOIN = 1 << 0
    """Display a message about new users joining."""

    SUPPRESS_PREMIUM_SUBSCRIPTION = 1 << 1
    """Display a message when the guild is Nitro boosted."""


@enum.unique
class GuildVerificationLevel(int, enum.Enum):
    """Represents the level of verification of a guild."""

    NONE = 0
    """Unrestricted"""

    LOW = 1
    """Must have a verified email on their account."""

    MEDIUM = 2
    """Must have been registered on Discord for more than 5 minutes."""

    HIGH = 3
    """(╯°□°）╯︵ ┻━┻ - must be a member of the guild for longer than 10 minutes."""

    VERY_HIGH = 4
    """┻━┻ミヽ(ಠ益ಠ)ﾉ彡┻━┻ - must have a verified phone number."""


@attr.s(eq=True, hash=False, init=False, kw_only=True, slots=True)
class GuildWidget(bases.Entity):
    """Represents a guild embed."""

    channel_id: typing.Optional[bases.Snowflake] = attr.ib(repr=True)
    """The ID of the channel the invite for this embed targets, if enabled."""

    is_enabled: bool = attr.ib(repr=True)
    """Whether this embed is enabled."""


@attr.s(eq=True, hash=True, init=False, kw_only=True, slots=True)
class GuildMember(bases.Entity):
    """Used to represent a guild bound member."""

    # TODO: make GuildMember delegate to user and implement a common base class
    # this allows members and users to be used interchangeably.
    user: users.User = attr.ib(eq=True, hash=True, repr=True)
    """This member's user object.

    This will be `None` when attached to Message Create and Update gateway events.
    """

    nickname: typing.Optional[str] = attr.ib(
        eq=False, hash=False, repr=True,
    )
    """This member's nickname, if set."""

    role_ids: typing.Set[bases.Snowflake] = attr.ib(
        eq=False, hash=False,
    )
    """A sequence of the IDs of the member's current roles."""

    joined_at: datetime.datetime = attr.ib(eq=False, hash=False)
    """The datetime of when this member joined the guild they belong to."""

    premium_since: typing.Optional[datetime.datetime] = attr.ib(eq=False, hash=False)
    """The datetime of when this member started "boosting" this guild.

    This will be `None` if they aren't boosting.
    """

    is_deaf: bool = attr.ib(eq=False, hash=False)
    """Whether this member is deafened by this guild in it's voice channels."""

    is_mute: bool = attr.ib(eq=False, hash=False)
    """Whether this member is muted by this guild in it's voice channels."""


@attr.s(eq=True, hash=True, init=False, kw_only=True, slots=True)
class PartialRole(bases.Entity, bases.Unique):
    """Represents a partial guild bound Role object."""

    name: str = attr.ib(eq=False, hash=False, repr=True)
    """The role's name."""


@attr.s(eq=True, hash=True, init=False, kw_only=True, slots=True)
class Role(PartialRole):
    """Represents a guild bound Role object."""

    color: colors.Color = attr.ib(
        eq=False, hash=False, repr=True,
    )
    """The colour of this role.

    This will be applied to a member's name in chat if it's their top coloured role.
    """

    is_hoisted: bool = attr.ib(eq=False, hash=False, repr=True)
    """Whether this role is hoisting the members it's attached to in the member list.

    members will be hoisted under their highest role where this is set to `True`.
    """

    position: int = attr.ib(eq=False, hash=False, repr=True)
    """The position of this role in the role hierarchy."""

    permissions: permissions_.Permission = attr.ib(eq=False, hash=False)
    """The guild wide permissions this role gives to the members it's attached to,

    This may be overridden by channel overwrites.
    """

    is_managed: bool = attr.ib(eq=False, hash=False)
    """Whether this role is managed by an integration."""

    is_mentionable: bool = attr.ib(eq=False, hash=False)
    """Whether this role can be mentioned by all regardless of permissions."""


@enum.unique
class ActivityType(int, enum.Enum):
    """The activity type."""

    PLAYING = 0
    """Shows up as `Playing <name>`"""

    STREAMING = 1

    LISTENING = 2
    """Shows up as `Listening to <name>`."""

    WATCHING = 3
    """Shows up as `Watching <name>`.

    !!! note
        this is not officially documented, so will be likely removed in the near
        future.
    """

    CUSTOM = 4
    """A custom status.

    To set an emoji with the status, place a unicode emoji or Discord emoji
    (`:smiley:`) as the first part of the status activity name.
    """


@attr.s(eq=True, hash=False, init=False, kw_only=True, slots=True)
class ActivityTimestamps:
    """The datetimes for the start and/or end of an activity session."""

    start: typing.Optional[datetime.datetime] = attr.ib(repr=True)
    """When this activity's session was started, if applicable."""

    end: typing.Optional[datetime.datetime] = attr.ib(repr=True)
    """When this activity's session will end, if applicable."""


@attr.s(eq=True, hash=True, init=False, kw_only=True, slots=True)
class ActivityParty:
    """Used to represent activity groups of users."""

    id: typing.Optional[str] = attr.ib(eq=True, hash=True, repr=True)
    """The string id of this party instance, if set."""

    current_size: typing.Optional[int] = attr.ib(eq=False, hash=False)
    """Current size of this party, if applicable."""

    max_size: typing.Optional[int] = attr.ib(eq=False, hash=False)
    """Maximum size of this party, if applicable."""


@attr.s(eq=True, hash=False, init=False, kw_only=True, slots=True)
class ActivityAssets:
    """Used to represent possible assets for an activity."""

    large_image: typing.Optional[str] = attr.ib()
    """The ID of the asset's large image, if set."""

    large_text: typing.Optional[str] = attr.ib()
    """The text that'll appear when hovering over the large image, if set."""

    small_image: typing.Optional[str] = attr.ib()
    """The ID of the asset's small image, if set."""

    small_text: typing.Optional[str] = attr.ib()
    """The text that'll appear when hovering over the small image, if set."""


@attr.s(eq=True, hash=False, init=False, kw_only=True, slots=True)
class ActivitySecret:
    """The secrets used for interacting with an activity party."""

    join: typing.Optional[str] = attr.ib()
    """The secret used for joining a party, if applicable."""

    spectate: typing.Optional[str] = attr.ib()
    """The secret used for spectating a party, if applicable."""

    match: typing.Optional[str] = attr.ib()
    """The secret used for joining a party, if applicable."""


@enum.unique
class ActivityFlag(enum.IntFlag):
    """Flags that describe what an activity includes.

    This can be more than one using bitwise-combinations.
    """

    INSTANCE = 1 << 0
    """Instance"""

    JOIN = 1 << 1
    """Join"""

    SPECTATE = 1 << 2
    """Spectate"""

    JOIN_REQUEST = 1 << 3
    """Join Request"""

    SYNC = 1 << 4
    """Sync"""

    PLAY = 1 << 5
    """Play"""


@attr.s(eq=True, hash=False, init=False, kw_only=True, slots=True)
class PresenceActivity:
    """Represents an activity that will be attached to a member's presence."""

    name: str = attr.ib(repr=True)
    """The activity's name."""

    type: ActivityType = attr.ib(repr=True)
    """The activity's type."""

    url: typing.Optional[str] = attr.ib()
    """The URL for a `STREAM` type activity, if applicable."""

    created_at: datetime.datetime = attr.ib()
    """When this activity was added to the user's session."""

    timestamps: typing.Optional[ActivityTimestamps] = attr.ib()
    """The timestamps for when this activity's current state will start and
    end, if applicable.
    """

    application_id: typing.Optional[bases.Snowflake] = attr.ib()
    """The ID of the application this activity is for, if applicable."""

    details: typing.Optional[str] = attr.ib()
    """The text that describes what the activity's target is doing, if set."""

    state: typing.Optional[str] = attr.ib()
    """The current status of this activity's target, if set."""

    emoji: typing.Union[None, emojis_.UnicodeEmoji, emojis_.CustomEmoji] = attr.ib()
    """The emoji of this activity, if it is a custom status and set."""

    party: typing.Optional[ActivityParty] = attr.ib()
    """Information about the party associated with this activity, if set."""

    assets: typing.Optional[ActivityAssets] = attr.ib()
    """Images and their hover over text for the activity."""

    secrets: typing.Optional[ActivitySecret] = attr.ib()
    """Secrets for Rich Presence joining and spectating."""

    is_instance: typing.Optional[bool] = attr.ib()
    """Whether this activity is an instanced game session."""

    flags: ActivityFlag = attr.ib()
    """Flags that describe what the activity includes."""


class PresenceStatus(str, enum.Enum):
    """The status of a member."""

    ONLINE = "online"
    """Online/green."""

    IDLE = "idle"
    """Idle/yellow."""

    DND = "dnd"
    """Do not disturb/red."""

    DO_NOT_DISTURB = DND
    """An alias for `PresenceStatus.DND`"""

    OFFLINE = "offline"
    """Offline or invisible/grey."""


@attr.s(eq=True, hash=False, init=False, kw_only=True, slots=True)
class ClientStatus:
    """The client statuses for this member."""

    desktop: PresenceStatus = attr.ib(repr=True)
    """The status of the target user's desktop session."""

    mobile: PresenceStatus = attr.ib(repr=True)
    """The status of the target user's mobile session."""

    web: PresenceStatus = attr.ib(repr=True)
    """The status of the target user's web session."""


# TODO: should this be an event instead?
@attr.s(eq=True, hash=True, init=False, kw_only=True, slots=True)
class PresenceUser(users.User):
    """A user representation specifically used for presence updates.

    !!! warning
        Every attribute except `PresenceUser.id` may be as `hikari.models.unset.UNSET`
        unless it is specifically being modified for this update.
    """

    discriminator: typing.Union[str, undefined.Undefined] = attr.ib(eq=False, hash=False, repr=True)
    """This user's discriminator."""

    username: typing.Union[str, undefined.Undefined] = attr.ib(eq=False, hash=False, repr=True)
    """This user's username."""

    avatar_hash: typing.Union[None, str, undefined.Undefined] = attr.ib(
        eq=False, hash=False, repr=True,
    )
    """This user's avatar hash, if set."""

    is_bot: typing.Union[bool, undefined.Undefined] = attr.ib(
        eq=False, hash=False, repr=True,
    )
    """Whether this user is a bot account."""

    is_system: typing.Union[bool, undefined.Undefined] = attr.ib(
        eq=False, hash=False,
    )
    """Whether this user is a system account."""

    flags: typing.Union[users.UserFlag, undefined.Undefined] = attr.ib(eq=False, hash=False)
    """The public flags for this user."""

    @property
    def avatar_url(self) -> typing.Union[str, undefined.Undefined]:
        """URL for this user's avatar if the relevant info is available.

        !!! note
            This will be `hikari.models.unset.UNSET` if both `PresenceUser.avatar_hash`
            and `PresenceUser.discriminator` are `hikari.models.unset.UNSET`.
        """
        return self.format_avatar_url()

    def format_avatar_url(
        self, *, format_: typing.Optional[str] = None, size: int = 4096
    ) -> typing.Union[str, undefined.Undefined]:
        """Generate the avatar URL for this user's avatar if available.

        Parameters
        ----------
        format_ : str
            The format to use for this URL, defaults to `png` or `gif`.
            Supports `png`, `jpeg`, `jpg`, `webp` and `gif` (when animated).
            Will be ignored for default avatars which can only be `png`.
        size : int
            The size to set for the URL, defaults to `4096`.
            Can be any power of two between 16 and 4096.
            Will be ignored for default avatars.

        Returns
        -------
        hikari.models.unset.UNSET | str
            The string URL of the user's custom avatar if
            either `PresenceUser.avatar_hash` is set or their default avatar if
            `PresenceUser.discriminator` is set, else `hikari.models.unset.UNSET`.

        Raises
        ------
        ValueError
            If `size` is not a power of two or not between 16 and 4096.
        """
        if self.discriminator is not undefined.Undefined() or self.avatar_hash is not undefined.Undefined():
            return super().format_avatar_url(format_=format_, size=size)
        return undefined.Undefined()

    @property
    def default_avatar_index(self) -> typing.Union[int, undefined.Undefined]:
        """Integer representation of this user's default avatar.

        !!! note
            This will be `hikari.models.unset.UNSET` if `PresenceUser.discriminator` is
            `hikari.models.unset.UNSET`.
        """
        if self.discriminator is not undefined.Undefined():
            return super().default_avatar_index
        return undefined.Undefined()

    @property
    def default_avatar_url(self) -> typing.Union[str, undefined.Undefined]:
        """URL for this user's default avatar.

        !!! note
            This will be `hikari.models.unset.UNSET` if `PresenceUser.discriminator` is
            `hikari.models.unset.UNSET`.
        """
        if self.discriminator is not undefined.Undefined():
            return super().default_avatar_url
        return undefined.Undefined()


@attr.s(eq=True, hash=True, init=False, kw_only=True, slots=True)
class GuildMemberPresence(bases.Entity):
    """Used to represent a guild member's presence."""

    user: PresenceUser = attr.ib(eq=True, hash=True, repr=True)
    """The object of the user who this presence is for.

    !!! info
        Only `PresenceUser.id` is guaranteed for this partial object,
        with other attributes only being included when when they are being
        changed in an event.
    """

    role_ids: typing.Optional[typing.Sequence[bases.Snowflake]] = attr.ib(
        eq=False, hash=False,
    )
    """The ids of the user's current roles in the guild this presence belongs to.

    !!! info
        If this is `None` then this information wasn't provided and is unknown.
    """

    guild_id: typing.Optional[bases.Snowflake] = attr.ib(eq=True, hash=True, repr=True)
    """The ID of the guild this presence belongs to.

    This will be `None` when received in an array of members attached to a guild
    object (e.g on Guild Create).
    """

    visible_status: PresenceStatus = attr.ib(eq=False, hash=False, repr=True)
    """This user's current status being displayed by the client."""

    activities: typing.Sequence[PresenceActivity] = attr.ib(eq=False, hash=False)
    """An array of the user's activities, with the top one will being
    prioritised by the client.
    """

    client_status: ClientStatus = attr.ib(
        eq=False, hash=False,
    )
    """An object of the target user's client statuses."""

    premium_since: typing.Optional[datetime.datetime] = attr.ib(
        eq=False, hash=False,
    )
    """The datetime of when this member started "boosting" this guild.

    This will be `None` if they aren't boosting.
    """

    nickname: typing.Optional[str] = attr.ib(
        eq=False, hash=False, repr=True,
    )
    """This member's nickname, if set."""


@enum.unique
class IntegrationExpireBehaviour(int, enum.Enum):
    """Behavior for expiring integration subscribers."""

    REMOVE_ROLE = 0
    """Remove the role."""

    KICK = 1
    """Kick the subscriber."""


@attr.s(eq=True, hash=True, init=False, kw_only=True, slots=True)
class IntegrationAccount:
    """An account that's linked to an integration."""

    id: str = attr.ib(eq=True, hash=True)
    """The string ID of this (likely) third party account."""

    name: str = attr.ib(eq=False, hash=False)
    """The name of this account."""


@attr.s(eq=True, hash=True, init=False, kw_only=True, slots=True)
class PartialIntegration(bases.Unique):
    """A partial representation of an integration, found in audit logs."""

    name: str = attr.ib(eq=False, hash=False, repr=True)
    """The name of this integration."""

    type: str = attr.ib(eq=False, hash=False, repr=True)
    """The type of this integration."""

    account: IntegrationAccount = attr.ib(eq=False, hash=False)
    """The account connected to this integration."""


@attr.s(eq=True, hash=True, init=False, kw_only=True, slots=True)
class Integration(PartialIntegration):
    """Represents a guild integration object."""

    is_enabled: bool = attr.ib(eq=False, hash=False, repr=True)
    """Whether this integration is enabled."""

    is_syncing: bool = attr.ib(eq=False, hash=False)
    """Whether this integration is syncing subscribers/emojis."""

    role_id: typing.Optional[bases.Snowflake] = attr.ib(eq=False, hash=False)
    """The ID of the managed role used for this integration's subscribers."""

    is_emojis_enabled: typing.Optional[bool] = attr.ib(eq=False, hash=False)
    """Whether users under this integration are allowed to use it's custom emojis."""

    expire_behavior: IntegrationExpireBehaviour = attr.ib(eq=False, hash=False)
    """How members should be treated after their connected subscription expires.

    This won't be enacted until after `GuildIntegration.expire_grace_period`
    passes.
    """

    expire_grace_period: datetime.timedelta = attr.ib(eq=False, hash=False)
    """How many days users with expired subscriptions are given until
    `GuildIntegration.expire_behavior` is enacted out on them
    """

    user: users.User = attr.ib(eq=False, hash=False)
    """The user this integration belongs to."""

    last_synced_at: datetime.datetime = attr.ib(eq=False, hash=False)
    """The datetime of when this integration's subscribers were last synced."""


@attr.s(eq=True, hash=False, init=False, kw_only=True, slots=True)
class GuildMemberBan:
    """Used to represent guild bans."""

    reason: typing.Optional[str] = attr.ib(repr=True)
    """The reason for this ban, will be `None` if no reason was given."""

    user: users.User = attr.ib(repr=True)
    """The object of the user this ban targets."""


@attr.s(eq=True, hash=True, init=False, kw_only=True, slots=True)
class UnavailableGuild(bases.Entity, bases.Unique):
    """An unavailable guild object, received during gateway events such as READY.

    An unavailable guild cannot be interacted with, and most information may
    be outdated if that is the case.
    """

    # Ignore docstring not starting in an imperative mood
    @property
    def is_unavailable(self) -> bool:  # noqa: D401
        """`True` if this guild is unavailable, else `False`.

        This value is always `True`, and is only provided for consistency.
        """
        return True


@attr.s(eq=True, hash=True, init=False, kw_only=True, slots=True)
class PartialGuild(bases.Entity, bases.Unique):
    """Base object for any partial guild objects."""

    name: str = attr.ib(eq=False, hash=False, repr=True)
    """The name of the guild."""

    icon_hash: typing.Optional[str] = attr.ib(eq=False, hash=False)
    """The hash for the guild icon, if there is one."""

    features: typing.Set[typing.Union[GuildFeature, str]] = attr.ib(eq=False, hash=False)
    """A set of the features in this guild."""

    def format_icon_url(self, *, format_: typing.Optional[str] = None, size: int = 4096) -> typing.Optional[str]:
        """Generate the URL for this guild's custom icon, if set.

        Parameters
        ----------
        format_ : str
            The format to use for this URL, defaults to `png` or `gif`.
            Supports `png`, `jpeg`, `jpg`, `webp` and `gif` (when
            animated).
        size : int
            The size to set for the URL, defaults to `4096`.
            Can be any power of two between 16 and 4096.

        Returns
        -------
        str | None
            The string URL.

        Raises
        ------
        ValueError
            If `size` is not a power of two or not between 16 and 4096.
        """
        if self.icon_hash:
            if format_ is None:
                format_ = "gif" if self.icon_hash.startswith("a_") else "png"
            return urls.generate_cdn_url("icons", str(self.id), self.icon_hash, format_=format_, size=size)
        return None

    @property
    def icon_url(self) -> typing.Optional[str]:
        """URL for this guild's icon, if set."""
        return self.format_icon_url()


@attr.s(eq=True, hash=True, init=False, kw_only=True, slots=True)
class GuildPreview(PartialGuild):
    """A preview of a guild with the `GuildFeature.PUBLIC` feature."""

    splash_hash: typing.Optional[str] = attr.ib(eq=False, hash=False)
    """The hash of the splash for the guild, if there is one."""

    discovery_splash_hash: typing.Optional[str] = attr.ib(
        eq=False, hash=False,
    )
    """The hash of the discovery splash for the guild, if there is one."""

    emojis: typing.Mapping[bases.Snowflake, emojis_.KnownCustomEmoji] = attr.ib(
        eq=False, hash=False,
    )
    """The mapping of IDs to the emojis this guild provides."""

    approximate_presence_count: int = attr.ib(eq=False, hash=False, repr=True)
    """The approximate amount of presences in guild."""

    approximate_member_count: int = attr.ib(eq=False, hash=False, repr=True)
    """The approximate amount of members in this guild."""

    description: typing.Optional[str] = attr.ib(eq=False, hash=False)
    """The guild's description, if set."""

    def format_splash_url(self, *, format_: str = "png", size: int = 4096) -> typing.Optional[str]:
        """Generate the URL for this guild's splash image, if set.

        Parameters
        ----------
        format_ : str
            The format to use for this URL, defaults to `png`.
            Supports `png`, `jpeg`, `jpg` and `webp`.
        size : int
            The size to set for the URL, defaults to `4096`.
            Can be any power of two between 16 and 4096.

        Returns
        -------
        str | None
            The string URL.

        Raises
        ------
        ValueError
            If `size` is not a power of two or not between 16 and 4096.
        """
        if self.splash_hash:
            return urls.generate_cdn_url("splashes", str(self.id), self.splash_hash, format_=format_, size=size)
        return None

    @property
    def splash_url(self) -> typing.Optional[str]:
        """URL for this guild's splash, if set."""
        return self.format_splash_url()

    def format_discovery_splash_url(self, *, format_: str = "png", size: int = 4096) -> typing.Optional[str]:
        """Generate the URL for this guild's discovery splash image, if set.

        Parameters
        ----------
        format_ : str
            The format to use for this URL, defaults to `png`.
            Supports `png`, `jpeg`, `jpg` and `webp`.
        size : int
            The size to set for the URL, defaults to `4096`.
            Can be any power of two between 16 and 4096.

        Returns
        -------
        str | None
            The string URL.

        Raises
        ------
        ValueError
            If `size` is not a power of two or not between 16 and 4096.
        """
        if self.discovery_splash_hash:
            return urls.generate_cdn_url(
                "discovery-splashes", str(self.id), self.discovery_splash_hash, format_=format_, size=size
            )
        return None

    @property
    def discovery_splash_url(self) -> typing.Optional[str]:
        """URL for this guild's discovery splash, if set."""
        return self.format_discovery_splash_url()


@attr.s(eq=True, hash=True, init=False, kw_only=True, slots=True)
class Guild(PartialGuild):  # pylint:disable=too-many-instance-attributes
    """A representation of a guild on Discord.

    !!! note
        If a guild object is considered to be unavailable, then the state of any
        other fields other than the `Guild.is_unavailable` and `Guild.id` are
        outdated or incorrect. If a guild is unavailable, then the contents of
        any other fields should be ignored.
    """

    splash_hash: typing.Optional[str] = attr.ib(eq=False, hash=False)
    """The hash of the splash for the guild, if there is one."""

    discovery_splash_hash: typing.Optional[str] = attr.ib(eq=False, hash=False)
    """The hash of the discovery splash for the guild, if there is one."""

    owner_id: bases.Snowflake = attr.ib(eq=False, hash=False, repr=True)
    """The ID of the owner of this guild."""

    my_permissions: permissions_.Permission = attr.ib(
        eq=False, hash=False,
    )
    """The guild-level permissions that apply to the bot user.

    This will not take into account permission overwrites or implied
    permissions (for example, ADMINISTRATOR implies all other permissions).

    This will be `None` when this object is retrieved through a RESTSession request
    rather than from the gateway.
    """

    region: str = attr.ib(eq=False, hash=False)
    """The voice region for the guild."""

    afk_channel_id: typing.Optional[bases.Snowflake] = attr.ib(eq=False, hash=False)
    """The ID for the channel that AFK voice users get sent to.

    If `None`, then no AFK channel is set up for this guild.
    """

    afk_timeout: datetime.timedelta = attr.ib(eq=False, hash=False)
    """Timeout for activity before a member is classed as AFK.

    How long a voice user has to be AFK for before they are classed as being
    AFK and are moved to the AFK channel (`Guild.afk_channel_id`).
    """

    is_embed_enabled: typing.Optional[bool] = attr.ib(eq=False, hash=False)
    """Defines if the guild embed is enabled or not.

    This information may not be present, in which case, it will be `None`
    instead. This will be `None` for guilds that the bot is not a member in.

    !!! deprecated
        Use `is_widget_enabled` instead.
    """

    embed_channel_id: typing.Optional[bases.Snowflake] = attr.ib(eq=False, hash=False)
    """The channel ID that the guild embed will generate an invite to.

    Will be `None` if invites are disabled for this guild's embed.

    !!! deprecated
        Use `widget_channel_id` instead.
    """

    verification_level: GuildVerificationLevel = attr.ib(eq=False, hash=False)
    """The verification level required for a user to participate in this guild."""

    default_message_notifications: GuildMessageNotificationsLevel = attr.ib(eq=False, hash=False)
    """The default setting for message notifications in this guild."""

    explicit_content_filter: GuildExplicitContentFilterLevel = attr.ib(eq=False, hash=False)
    """The setting for the explicit content filter in this guild."""

    roles: typing.Mapping[bases.Snowflake, Role] = attr.ib(
        eq=False, hash=False,
    )
    """The roles in this guild, represented as a mapping of ID to role object."""

    emojis: typing.Mapping[bases.Snowflake, emojis_.KnownCustomEmoji] = attr.ib(eq=False, hash=False)
    """A mapping of IDs to the objects of the emojis this guild provides."""

    mfa_level: GuildMFALevel = attr.ib(eq=False, hash=False)
    """The required MFA level for users wishing to participate in this guild."""

    application_id: typing.Optional[bases.Snowflake] = attr.ib(eq=False, hash=False)
    """The ID of the application that created this guild.

    This will always be `None` for guilds that weren't created by a bot.
    """

    is_unavailable: typing.Optional[bool] = attr.ib(eq=False, hash=False)
    """Whether the guild is unavailable or not.

    This information is only available if the guild was sent via a
    `GUILD_CREATE` event. If the guild is received from any other place, this
    will always be `None`.

    An unavailable guild cannot be interacted with, and most information may
    be outdated if that is the case.
    """

    is_widget_enabled: typing.Optional[bool] = attr.ib(eq=False, hash=False)
    """Describes whether the guild widget is enabled or not.

    If this information is not present, this will be `None`.
    """

    widget_channel_id: typing.Optional[bases.Snowflake] = attr.ib(eq=False, hash=False)
    """The channel ID that the widget's generated invite will send the user to.

    If this information is unavailable or this isn't enabled for the guild then
    this will be `None`.
    """

    system_channel_id: typing.Optional[bases.Snowflake] = attr.ib(eq=False, hash=False)
    """The ID of the system channel or `None` if it is not enabled.

    Welcome messages and Nitro boost messages may be sent to this channel.
    """

    system_channel_flags: GuildSystemChannelFlag = attr.ib(eq=False, hash=False)
    """Flags for the guild system channel to describe which notifications are suppressed."""

    rules_channel_id: typing.Optional[bases.Snowflake] = attr.ib(eq=False, hash=False)
    """The ID of the channel where guilds with the `GuildFeature.PUBLIC`
    `features` display rules and guidelines.

    If the `GuildFeature.PUBLIC` feature is not defined, then this is `None`.
    """

    joined_at: typing.Optional[datetime.datetime] = attr.ib(eq=False, hash=False)
    """The date and time that the bot user joined this guild.

    This information is only available if the guild was sent via a `GUILD_CREATE`
    event. If the guild is received from any other place, this will always be
    `None`.
    """

    is_large: typing.Optional[bool] = attr.ib(eq=False, hash=False)
    """Whether the guild is considered to be large or not.

    This information is only available if the guild was sent via a `GUILD_CREATE`
    event. If the guild is received from any other place, this will always be
    `None`.

    The implications of a large guild are that presence information will not be
    sent about members who are offline or invisible.
    """

    member_count: typing.Optional[int] = attr.ib(eq=False, hash=False)
    """The number of members in this guild.

    This information is only available if the guild was sent via a `GUILD_CREATE`
    event. If the guild is received from any other place, this will always be
    `None`.
    """

    members: typing.Optional[typing.Mapping[bases.Snowflake, GuildMember]] = attr.ib(eq=False, hash=False)
    """A mapping of ID to the corresponding guild members in this guild.

    This information is only available if the guild was sent via a `GUILD_CREATE`
    event. If the guild is received from any other place, this will always be
    `None`.

    Additionally, any offline members may not be included here, especially if
    there are more members than the large threshold set for the gateway this
    object was send with.

    This information will only be updated if your shards have the correct
    intents set for any update events.

    Essentially, you should not trust the information here to be a full
    representation. If you need complete accurate information, you should
    query the members using the appropriate API call instead.
    """

    channels: typing.Optional[typing.Mapping[bases.Snowflake, channels_.GuildChannel]] = attr.ib(
        eq=False, hash=False,
    )
    """A mapping of ID to the corresponding guild channels in this guild.

    This information is only available if the guild was sent via a `GUILD_CREATE`
    event. If the guild is received from any other place, this will always be
    `None`.

    Additionally, any channels that you lack permissions to see will not be
    defined here.

    This information will only be updated if your shards have the correct
    intents set for any update events.

    To retrieve a list of channels in any other case, you should make an
    appropriate API call to retrieve this information.
    """

    presences: typing.Optional[typing.Mapping[bases.Snowflake, GuildMemberPresence]] = attr.ib(
        eq=False, hash=False,
    )
    """A mapping of member ID to the corresponding presence information for
    the given member, if available.

    This information is only available if the guild was sent via a `GUILD_CREATE`
    event. If the guild is received from any other place, this will always be
    `None`.

    Additionally, any channels that you lack permissions to see will not be
    defined here.

    This information will only be updated if your shards have the correct
    intents set for any update events.

    To retrieve a list of presences in any other case, you should make an
    appropriate API call to retrieve this information.
    """

    max_presences: typing.Optional[int] = attr.ib(eq=False, hash=False)
    """The maximum number of presences for the guild.

    If this is `None`, then the default value is used (currently 25000).
    """

    max_members: typing.Optional[int] = attr.ib(eq=False, hash=False)
    """The maximum number of members allowed in this guild.

    This information may not be present, in which case, it will be `None`.
    """

    max_video_channel_users: typing.Optional[int] = attr.ib(eq=False, hash=False)
    """The maximum number of users allowed in a video channel together.

    This information may not be present, in which case, it will be `None`.
    """

    vanity_url_code: typing.Optional[str] = attr.ib(eq=False, hash=False)
    """The vanity URL code for the guild's vanity URL.

    This is only present if `GuildFeature.VANITY_URL` is in `Guild.features` for
    this guild. If not, this will always be `None`.
    """

    description: typing.Optional[str] = attr.ib(eq=False, hash=False)
    """The guild's description.

    This is only present if certain `GuildFeature`'s are set in
    `Guild.features` for this guild. Otherwise, this will always be `None`.
    """

    banner_hash: typing.Optional[str] = attr.ib(eq=False, hash=False)
    """The hash for the guild's banner.

    This is only present if the guild has `GuildFeature.BANNER` in
    `Guild.features` for this guild. For all other purposes, it is `None`.
    """

    premium_tier: GuildPremiumTier = attr.ib(eq=False, hash=False)
    """The premium tier for this guild."""

    premium_subscription_count: typing.Optional[int] = attr.ib(eq=False, hash=False)
    """The number of nitro boosts that the server currently has.

    This information may not be present, in which case, it will be `None`.
    """

    preferred_locale: str = attr.ib(eq=False, hash=False)
    """The preferred locale to use for this guild.

    This can only be change if `GuildFeature.PUBLIC` is in `Guild.features`
    for this guild and will otherwise default to `en-US`.
    """

    public_updates_channel_id: typing.Optional[bases.Snowflake] = attr.ib(eq=False, hash=False)
    """The channel ID of the channel where admins and moderators receive notices
    from Discord.

    This is only present if `GuildFeature.PUBLIC` is in `Guild.features` for
    this guild. For all other purposes, it should be considered to be `None`.
    """

    # TODO: if this is `None`, then should we attempt to look at the known member count if present?
    approximate_member_count: typing.Optional[int] = attr.ib(eq=False, hash=False)
    """The approximate number of members in the guild.

    This information will be provided by RESTSession API calls fetching the guilds that
    a bot account is in. For all other purposes, this should be expected to
    remain `None`.
    """

    approximate_active_member_count: typing.Optional[int] = attr.ib(eq=False, hash=False)
    """The approximate number of members in the guild that are not offline.

    This information will be provided by RESTSession API calls fetching the guilds that
    a bot account is in. For all other purposes, this should be expected to
    remain `None`.
    """

    def format_splash_url(self, *, format_: str = "png", size: int = 4096) -> typing.Optional[str]:
        """Generate the URL for this guild's splash image, if set.

        Parameters
        ----------
        format_ : str
            The format to use for this URL, defaults to `png`.
            Supports `png`, `jpeg`, `jpg` and `webp`.
        size : int
            The size to set for the URL, defaults to `4096`.
            Can be any power of two between 16 and 4096.

        Returns
        -------
        str | None
            The string URL.

        Raises
        ------
        ValueError
            If `size` is not a power of two or not between 16 and 4096.
        """
        if self.splash_hash:
            return urls.generate_cdn_url("splashes", str(self.id), self.splash_hash, format_=format_, size=size)
        return None

    @property
    def splash_url(self) -> typing.Optional[str]:
        """URL for this guild's splash, if set."""
        return self.format_splash_url()

    def format_discovery_splash_url(self, *, format_: str = "png", size: int = 4096) -> typing.Optional[str]:
        """Generate the URL for this guild's discovery splash image, if set.

        Parameters
        ----------
        format_ : str
            The format to use for this URL, defaults to `png`.
            Supports `png`, `jpeg`, `jpg` and `webp`.
        size : int
            The size to set for the URL, defaults to `4096`.
            Can be any power of two between 16 and 4096.

        Returns
        -------
        str | None
            The string URL.

        Raises
        ------
        ValueError
            If `size` is not a power of two or not between 16 and 4096.
        """
        if self.discovery_splash_hash:
            return urls.generate_cdn_url(
                "discovery-splashes", str(self.id), self.discovery_splash_hash, format_=format_, size=size
            )
        return None

    @property
    def discovery_splash_url(self) -> typing.Optional[str]:
        """URL for this guild's discovery splash, if set."""
        return self.format_discovery_splash_url()

    def format_banner_url(self, *, format_: str = "png", size: int = 4096) -> typing.Optional[str]:
        """Generate the URL for this guild's banner image, if set.

        Parameters
        ----------
        format_ : str
            The format to use for this URL, defaults to `png`.
            Supports `png`, `jpeg`, `jpg` and `webp`.
        size : int
            The size to set for the URL, defaults to `4096`.
            Can be any power of two between 16 and 4096.

        Returns
        -------
        str | None
            The string URL.

        Raises
        ------
        ValueError
            If `size` is not a power of two or not between 16 and 4096.
        """
        if self.banner_hash:
            return urls.generate_cdn_url("banners", str(self.id), self.banner_hash, format_=format_, size=size)
        return None

    @property
    def banner_url(self) -> typing.Optional[str]:
        """URL for this guild's banner, if set."""
        return self.format_banner_url()
