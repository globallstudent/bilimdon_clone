from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.database import Base

class GameStatus(str, enum.Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class Tournament(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    created_by = Column(Integer, ForeignKey("users.id"))
    status = Column(Enum(GameStatus), default=GameStatus.SCHEDULED)
    
    tournament_games = relationship("TournamentGame", back_populates="tournament")
    participants = relationship("TournamentParticipant", back_populates="tournament")

class TournamentGame(Base):
    __tablename__ = "tournament_games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    tournament_id = Column(Integer, ForeignKey("tournaments.id"))
    status = Column(Enum(GameStatus), default=GameStatus.SCHEDULED)
    
    tournament = relationship("Tournament", back_populates="tournament_games")
    questions = relationship("TournamentQuestion", back_populates="game")
    participants = relationship("GameParticipant", back_populates="game")

class TournamentQuestion(Base):
    __tablename__ = "tournament_questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, nullable=False)
    correct_answer = Column(String, nullable=False)
    game_id = Column(Integer, ForeignKey("tournament_games.id"))
    points = Column(Integer, default=1)
    
    game = relationship("TournamentGame", back_populates="questions")
    options = relationship("TournamentQuestionOption", back_populates="question")

class TournamentQuestionOption(Base):
    __tablename__ = "tournament_question_options"

    id = Column(Integer, primary_key=True, index=True)
    option_text = Column(String, nullable=False)
    question_id = Column(Integer, ForeignKey("tournament_questions.id"))
    
    question = relationship("TournamentQuestion", back_populates="options")

class TournamentParticipant(Base):
    __tablename__ = "tournament_participants"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    tournament_id = Column(Integer, ForeignKey("tournaments.id"))
    joined_at = Column(DateTime, default=datetime.utcnow)
    total_score = Column(Integer, default=0)
    
    tournament = relationship("Tournament", back_populates="participants")
    game_participations = relationship("GameParticipant", back_populates="tournament_participant")

class GameParticipant(Base):
    __tablename__ = "tournament_game_participants"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    game_id = Column(Integer, ForeignKey("tournament_games.id"))
    tournament_participant_id = Column(Integer, ForeignKey("tournament_participants.id"))
    score = Column(Integer, default=0)
    joined_at = Column(DateTime, default=datetime.utcnow)
    
    game = relationship("TournamentGame", back_populates="participants")
    tournament_participant = relationship("TournamentParticipant", back_populates="game_participations")
    answers = relationship("PlayerAnswer", back_populates="game_participant")

class PlayerAnswer(Base):
    __tablename__ = "tournament_player_answers"

    id = Column(Integer, primary_key=True, index=True)
    game_participant_id = Column(Integer, ForeignKey("tournament_game_participants.id"))
    question_id = Column(Integer, ForeignKey("tournament_questions.id"))
    answer = Column(String)
    is_correct = Column(Boolean)
    answered_at = Column(DateTime, default=datetime.utcnow)
    
    game_participant = relationship("GameParticipant", back_populates="answers") 