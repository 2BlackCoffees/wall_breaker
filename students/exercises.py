from typing import List, Tuple
from services.game_state import GameState

class Exercises:

    @staticmethod
    def init_game_values() -> Tuple[int, int, int]:
        """
        When the user lost or the game starts, we need to define 
        * the number of balls for the new game
        * the initial score
        * which game we want the user starts with
        """
        number_balls: int = 3
        current_score: int = 0
        game_index: int = 0
        return (number_balls, current_score, game_index)

    @staticmethod
    def new_number_balls_after_a_ball_was_missed(
          current_number_balls: int) -> int:
        """
        A ball was missed by the player so 
        we need to tell the game how many remaining balls there are...
        """
        return current_number_balls - 1

    @staticmethod
    def restart_from_first_scene_after_last_scene(
            current_scene_number:int, 
            number_of_scenes: int) -> int:
        """
        Return either the current scene number 
        if is is below number_of_scenes
        Otherwise return 0
        """
        if current_scene_number >= number_of_scenes:
            return 0
        else:
            return current_scene_number
    @staticmethod
    def return_game_name(
            index_of_list:int, 
            list_of_games: List[str]) -> str:
        """
        Return the element of the list pointed
        by the index of the list.
        Bonus: Return the first element 
        if the index is bigger than the size of the list
        """
        if index_of_list < len(list_of_games):
            return list_of_games[index_of_list]
        return list_of_games[0]
    @staticmethod
    def get_next_state(game_state: GameState) -> GameState:
        """
        We define here a state machine.
        In Software a state machine is an algorithm whose state define what the program should be doing.
        These state can change and the next state is usally strongly coupled with the previous state.

        In other words we expect the following:
        GameState.ASKING_USER_NAME -> GameState.SHOWING_SCORE
        GameState.SHOWING_SCORE -> GameState.PLAYING
        GameState.WAITING_PLAYER_READY_BEFORE_GAME_RESTART -> GameState.PLAYING
        GameState.WAITING_PLAYER_READY_BEFORE_NEXT_LEVEL -> GameState.PLAYING
        """
        if game_state == GameState.ASKING_USER_NAME:
            game_state = GameState.SHOWING_SCORE
        elif game_state in [ GameState.SHOWING_SCORE,
                                  GameState.WAITING_PLAYER_READY_BEFORE_GAME_RESTART ]:
            game_state = GameState.PLAYING
        elif game_state == GameState.WAITING_PLAYER_READY_BEFORE_LEVEL_REPLAY:
            game_state = GameState.PLAYING
        elif game_state == GameState.WAITING_PLAYER_READY_BEFORE_NEXT_LEVEL:
            game_state = GameState.PLAYING
        return game_state
    @staticmethod
    def get_next_state_when_lost(remaining_balls: int, 
                                 user_is_elected_to_wall_of_fame: bool) -> GameState:
        """
        This is the second part of the state machine

        This time the user just missed a ball, so we have the follwing cases:
        * The use missed a ball but there are more balls to play (meaning remaining_balls is greater than 0)
          -> go to state GameState.WAITING_PLAYER_READY_BEFORE_LEVEL_REPLAY
        * There are 0 or less balls
          * the user is elected for the wall of fames (user_is_elected_to_wall_of_fame is True)
            -> go to state GameState.ASKING_USER_NAME to ask the user his name
          * otherwise 
            -> go to state GameState.WAITING_PLAYER_READY_BEFORE_GAME_RESTART
        """
        if remaining_balls > 0:
            game_state = GameState.WAITING_PLAYER_READY_BEFORE_LEVEL_REPLAY
        else:
            if user_is_elected_to_wall_of_fame:
                game_state = GameState.ASKING_USER_NAME
            else:
                game_state = GameState.WAITING_PLAYER_READY_BEFORE_GAME_RESTART
        return game_state

    @staticmethod
    def get_initial_state() -> GameState:
        """
        This is the state the game will start with, you will need that later on
        """
        return GameState.WAITING_PLAYER_READY_BEFORE_LEVEL_REPLAY

    @staticmethod
    def get_sorted_new_score_list(user_name: str, score: int, 
                                  score_list: List[Tuple[str, int]], 
                                  max_scores: int = 10) -> None:
        """
        A list of score is a list composed of a tuple of a string (the name of the player) and an integer (its score)
        The list that we get is ordered with the old scores, a new score is now achieved.
        This new score must be placed at the correct position: position 0 is the best score, position 9 is the worst score

        Here the variable score_list (which is a list) is passed by reference (not very important to understand in detail, 
           but we do not need to return a new list as we are modifyig the variable in place)

        Here we must:
        1. Simply append a new tuple to the list if the list is empty
        2. If the list is not empty:
          a. Iterate over all elements of the list starting from the highest score
          b. If the variable score provided in the variable score is greater than the score in the list
             then the position should be used for the user ans score 
          c. Remember that the other scores must not be lost
          d. We want only 10 scores in the variable score_list
        
        """
        if len(score_list) == 0:
            score_list.append((user_name, score))
        else:
            add_index = len(score_list)
            for index in range(0, len(score_list)):
                _, cur_score = score_list[index]
                if score > cur_score:
                    add_index = index
                    break
            if add_index < len(score_list):
                new_score_list: List[Tuple[str, int]] = []
                if add_index > 0:
                    new_score_list = score_list[0:add_index]
                new_score_list.append((user_name, score))
                new_score_list.extend(score_list[add_index:])
                score_list = new_score_list
            else:
                score_list.append((user_name, score))

        if len(score_list) > max_scores:
            score_list = score_list[0:10]