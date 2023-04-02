from math import sqrt

# ex1 = "my string"
#
# ex2 = "5 dollar"
#
# ex3 = "6 cents"
#
#
# def str_to_list(a_string: str):
#     new_string = []
#     for i in range(len(a_string)):
#         c = a_string[i]
#         if c != " ":
#             try:
#                 if (int(c)) < 5:
#                     new_string.append(c)
#                     print("added to new string")
#                     print(f"new_string: {new_string}")
#             except ValueError:
#                 new_string.append(c)
#             finally:
#                 continue
#         else:
#             continue
#
#     return new_string
#
#
# re1 = str_to_list(ex1)
# re2 = str_to_list(ex2)
# re3 = str_to_list(ex3)
#
# print(re1)
# print(re2)
# print(re3)


# students = [("Allen Anderson", "Computer Science"),
#             ("Edgar Einstein", "Engineering"),
#             ("Farrah Finn", "Fine Arts")]
#
#
# def add_new_student(students, name, major):
#     students.append((name, major))
#
#
# def update_student(students, index, name, major):
#     students[index] = (name, major)
#
#
# def find_students_by_name(students, name):
#     return [student for student in students if name in student[0]]
#
#
# def get_all_majors(students):
#     return [student[1] for student in students]
#
#
if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }

    def group_by_owners(file):
        new_dict = {}
        for key in file:
            name = file[key]
            if name not in list(new_dict.keys()):
                new_dict[name] = [key]
            else:
                new_dict[name].append(key)
        return new_dict

    a_dict = group_by_owners(files)
    print(a_dict)
    print(group_by_owners(files))


# def find_roots1(a, b, c):
#     negative = ""
#     positive = ""
#     numerator = (b**2 - 4*a*c)
#     numerator = sqrt(abs(numerator))
#     print(numerator)
#     if numerator > 0:
#         positive = ((-b + numerator) / (2 * a))
#         negative = ((-b - numerator) / (2 * a))
#         print("real and different roots")
#         return negative, positive
#
#     elif numerator == 0:
#         print("real and same roots")
#         positive = (-b / (2 * a))
#         return positive
#
#     else:
#         print("complex roots")
#         negative = (- b / (2 * a), " + i", numerator)
#         positive = (- b / (2 * a), " - i", numerator)
#         return negative, positive
#
#     # denominator = 2 * a
#     # negative = -b + numerator/denominator
#     # positive = -b - numerator/denominator
#     return negative, positive
#
#
# # def find_roots(a, b, c):
# #     divisor = sqrt(b**2 - 4*a*c)
# #     negative = (-b + divisor)/2 * a
# #     positive = (-b - divisor)/2 * a
# #     return negative, positive
#
#
# # -10 - sqrt(10^2 - 4*2*8) / 4
# # -10 + sqrt(10^2 - 4*2*8) / 4
#
# # print(find_roots(2, 10, 8))
#
# print(find_roots1(2, 10, 8))
# print(find_roots1(1, 10, -24))

# class IceCreamMachine:
#
#     def __init__(self, ingredients, toppings):
#         self.ingredients = ingredients
#         self.toppings = toppings
#
#     def scoops(self):
#         scoop_list = []
#         for ingredient in self.ingredients:
#             for topping in self.toppings:
#                 scoop_list.append([ingredient, topping])
#         # return [[ingredient, self.toppings[0]] for ingredient in self.ingredients]
#         return scoop_list
#
#
# if __name__ == "__main__":
#     machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
#     print(machine.scoops())  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]




# if __name__ == "__main__":
#     files = {
#         'Input.txt': 'Randy',
#         'Code.py': 'Stan',
#         'Output.txt': 'Randy'
#     }
#
#
#     def group_by_owners(files):
#         return None
#
#
#     print(group_by_owners(files))