# Penguin Olympics: Swimming Race Disaster

def calculate_winners(snapshot, penguins):
    def score(lane):
        remaining = lane[lane.lower().index('p'):-1]
        return len(remaining) + remaining.count('~')

    ranking = dict(zip(penguins, map(score, snapshot.splitlines())))
    return "GOLD: {}, SILVER: {}, BRONZE: {}".format(*sorted(ranking, key=ranking.get))


snapshot = '''|----'p---~---------|
            |----p---~~--------|
            |----p---~~~-------|'''
penguins = ["Derek", "Francis", "Bob"]
print(calculate_winners(snapshot, penguins))


snapshot = '''|-~~------------~--P-------|
            |~~--~P------------~-------|
            |--------~-P---------------|
            |--------~-P----~~~--------|'''
penguins = ["Joline", "Abigail", "Jane", "Gerry"]
print(calculate_winners(snapshot, penguins))
