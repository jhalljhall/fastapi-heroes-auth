from typing import List, Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Table

class Base (DeclarativeBase):
    pass

class Hero(Base):
    __tablename__ = "heroes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = Column(String, default="Name")
    about_me: Mapped[str] =  Column(String, default="About me")
    biography: Mapped[str] =  Column(Text, default="Bio")
    image_url: Mapped[str] =  Column(String, default="img url")

    # what goes here? abilities, relationships
    abilities: Mapped[List["Ability"]] = relationship(back_populates="heroes", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Hero(id={self.id!r}, name={self.name!r}, about_me={self.about_me!r}, biography={self.biography!r}, image_url={self.image_url!r})"

class Ability(Base):
    __tablename__ = "abilities"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    ability_type_id: Mapped[int] = mapped_column(ForeignKey("ability_types.id"))
    hero_id: Mapped[int] = mapped_column(ForeignKey("heroes.id"))

    ability_types: Mapped["AbilityType"] = relationship(back_populates="abilities")

    heroes: Mapped["Hero"] = relationship(back_populates="abilities")

    def __repr__(self) -> str:
        return f"Ability(id={self.id!r}, ability_type_id={self.ability_type_id!r}, hero_id={self.hero_id!r})"

class Relationship(Base):
    __tablename__ = "relationships"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    hero1_id: Mapped[int] = Column(Integer, ForeignKey('heroes.id'))
    hero2_id: Mapped[int] = Column(Integer, ForeignKey('heroes.id'))
    relationship_type_id: Mapped[int] = mapped_column(ForeignKey("relationship_types.id"))

    def __repr__(self) -> str:
        return f"""Relationship(id={self.id!r}, 
                hero1_id={self.hero1_id!r}, 
                hero2_id={self.hero2_id!r}, 
                relationship_type_id={self.relationship_type_id!r})"""

class AbilityType(Base):
    __tablename__ = "ability_types"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30))

    abilities: Mapped[List["Ability"]] = relationship(
        back_populates="ability_types", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"AbilityType(id={self.id!r}, name={self.name!r})"

class RelationshipType(Base):

    __tablename__ = "relationship_types"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"RelationshipType(id={self.id!r}, name={self.name!r})"

