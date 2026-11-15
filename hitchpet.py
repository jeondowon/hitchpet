import random

ORDER = ["물", "산", "바람", "바다", "빛", "어둠", "도시", "전기", "동행"]
NAMES = {"물": "비 수달", "산": "지역 사슴", "바람": "장거리 레서판다", "바다": "바다 물범",
         "빛": "빛 사자", "어둠": "밤 여우", "도시": "도시 고양이", "전기": "전기 고슴도치", "동행": "동행 강아지"}


class Pet:
    def __init__(self, t):
        self.type, self.name = t, NAMES[t]
        self.hp = self.max_hp = 100
        self.atk = random.randint(15, 25)

    def alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}({self.type}) HP {max(self.hp, 0)}/{self.max_hp}"


def multiplier(a, d):
    diff = (ORDER.index(d) - ORDER.index(a)) % 9
    return 1.5 if diff in (1, 2) else 0.75 if diff in (7, 8) else 1.0


def attack(a, d):
    dmg = round(a.atk * multiplier(a.type, d.type))
    d.hp -= dmg
    print(f"{a.name} → {d.name} {dmg} 피해 (x{multiplier(a.type, d.type)})")


def pick_team(label):
    return [Pet(t) for t in random.sample(ORDER, 3)]


def main():
    me, foe = pick_team("나"), pick_team("상대")
    print("내 팀:", ", ".join(map(str, me)))
    print("상대 팀:", ", ".join(map(str, foe)))
    while any(p.alive() for p in me) and any(p.alive() for p in foe):
        mine = [p for p in me if p.alive()]
        for i, p in enumerate(mine):
            print(f"{i + 1}. {p}")
        try:
            a = mine[int(input("공격할 펫 번호: ")) - 1]
        except (ValueError, IndexError):
            continue
        theirs = [p for p in foe if p.alive()]
        for i, p in enumerate(theirs):
            print(f"{i + 1}. {p}")
        try:
            d = theirs[int(input("대상 번호: ")) - 1]
        except (ValueError, IndexError):
            continue
        attack(a, d)
        theirs = [p for p in foe if p.alive()]
        if theirs:
            attack(random.choice(theirs), random.choice([p for p in me if p.alive()]))
    print("승리! 랜드마크를 차지했습니다." if any(p.alive() for p in me) else "패배...")


if __name__ == "__main__":
    main()
