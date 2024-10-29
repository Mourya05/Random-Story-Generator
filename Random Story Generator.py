import random

characters = ["a brave knight", "a clever detective", "a mischievous cat", "an adventurous astronaut", "a curious child", 
              "a magical wizard", "an old pirate", "a talking robot", "a daring explorer", "a secretive spy"]

settings = ["in a haunted castle", "on a distant planet", "in a bustling city", "in a quiet village", "in an enchanted forest", 
            "at the bottom of the ocean", "in a futuristic metropolis", "in an ancient temple", "in a hidden cave", "in a snowy mountain"]

plots = ["who discovers a hidden treasure", "who saves the day", "who befriends an unlikely ally", "who uncovers a dark secret", 
         "who solves an ancient mystery", "who defeats a powerful enemy", "who escapes from a dangerous place", 
         "who finds a magical artifact", "who builds an incredible invention", "who unravels a complex conspiracy"]

times = ["during a stormy night", "in the midst of a war", "at the break of dawn", "under a full moon", "in the height of summer",
         "on the night of a festival", "during a solar eclipse", "in the early hours of the morning", "in the dead of winter", 
         "on a quiet Sunday afternoon"]

goals = ["to find the key to eternal life", "to save their best friend", "to stop a terrible disaster", "to uncover the truth",
         "to rescue a lost prince", "to return to their homeland", "to discover a new world", "to defeat an ancient curse",
         "to win the grand tournament", "to uncover a hidden kingdom"]

obstacles = ["facing fierce storms", "being chased by a shadowy figure", "trapped in a labyrinth", "with limited time",
             "lost in an unknown place", "betrayed by a close ally", "being hunted by a monster", "with magical powers failing",
             "with dwindling supplies", "haunted by their past mistakes"]

twists = ["but nothing is as it seems", "only to realize they are the villain", "discovering a long-lost sibling",
          "who turns out to be a ghost", "with a shocking betrayal from their ally", "and they must sacrifice something dear",
          "only to wake up from a dream", "and gain a surprising ally", "who was under a powerful spell", "that changes the course of history"]

def generate_expanded_story():
    character = random.choice(characters)
    setting = random.choice(settings)
    plot = random.choice(plots)
    time = random.choice(times)
    goal = random.choice(goals)
    obstacle = random.choice(obstacles)
    twist = random.choice(twists)

    return (f"Once upon a time, there was {character} {setting} {time}. The character's mission was {goal}, "
            f"while {obstacle}. Along the way, {plot}, {twist}.")

print(generate_expanded_story())
