import random
import copy

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        if not kwargs:
            raise ValueError("At least one variable is required")
        for name, value in kwargs.items():
            if isinstance(value, int):
                setattr(self, name, value)
                for i in range (value):
                    self.contents.append(name)
            else:
                print("pleas put an integer number as value")
        self.copy = self.contents.copy()

    def draw(self, number):
        all_remove = []
        if number > len(self.contents):
            return self.contents
        for i in range(number):
            remove = self.contents.pop(int(random.random() * len(self.contents)))
            all_remove.append(remove)
        return all_remove

    # def draw(self, number_balls):
    #     ball_in_hat = len(self.contents)
    #     if number_balls <= ball_in_hat:
    #         random_item = random.sample(self.contents, number_balls)
    #         for i in random_item:
    #             self.contents.remove(i)
    #         # print(random_item)
    #         # print(self.contents)
    #     else:
    #         # random_item = self.contents
    #         self.contents = self.copy
    #         random_item = self.contents
    #         # print(self.contents)
    #         # for name, value in vars(self).items():
    #         #     if isinstance(value, int):
    #         #         for i in range (value):
    #         #             self.contents.append(name)
    #         # print(self.contents)
    #         # random_item = random.sample(self.contents, number_balls)
    #         # for i in random_item:
    #         #     self.contents.remove(i)
    #     return random_item

def check_list(list1, list2):
    count1 = {}
    count2 = {}
    for item in list1:
        count1[item] = count1.get(item, 0) + 1
    for item in list2:
        count2[item] = count2.get(item, 0) + 1
    for item, count in count1.items():
        if item not in count2 or count2[item] < count:
            return False
    return True
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    N = 0
    list = []
    for item in expected_balls:
        for i in range (expected_balls[item]):
            list.append(item)
    for i in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        drawn_item = copy_hat.draw(num_balls_drawn)
        check = check_list(list, drawn_item)
        if check is True:
            M += 1
            print("found it", drawn_item)
        else:
            print("oops", drawn_item)
    return (M/num_experiments)

random.seed(95)

# hat1 = Hat(orange=2, yellow=8, blue=3)
hat = Hat(blue=3,red=2,green=6)
# print(hat1.draw(3))
# print(hat1.draw(5))
# print(hat1.draw(6))
# print(hat1.draw(6))

# print(experiment(hat1, {'blue':2, 'yellow':1}, 5, 10))
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print(probability)
# print(hat.draw(5))
# print(hat.draw(5))
# print(hat.draw(5))
# print(hat.draw(5))