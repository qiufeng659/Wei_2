import numpy as np
import matplotlib.pyplot as plt


class Function:
    def __init__(self, expression):
        self.expression = expression
        self.safe_dict = {
            "x": None,
            "np": np,
            "sin": np.sin,
            "cos": np.cos,
            "tan": np.tan,
            "exp": np.exp,
            "log": np.log,
            "sqrt": np.sqrt,
            "pi": np.pi,
            "e": np.e
        }

    def evaluate(self, x):
        try:
            self.safe_dict["x"] = x
            expr = self.expression.replace("^", "**")  # 自动修正输入
            return eval(expr, {"__builtins__": {}}, self.safe_dict)
        except Exception as e:
            print(f"Function error: {self.expression} -> {e}")
            return None


class Plotter:
    def plot(self, functions, x_min=-10, x_max=10, save=False):
        x = np.linspace(x_min, x_max, 500)

        plt.figure(figsize=(8, 6))

        for func in functions:
            y = func.evaluate(x)
            if y is not None:
                plt.plot(x, y, label=func.expression)

        plt.axhline(0)
        plt.axvline(0)
        plt.grid(True)
        plt.legend()
        plt.title("Function Visualization System")

        if save:
            plt.savefig("result.png")
            print("The image has been saved as result.png")

        plt.show()

class UserInterface:
    def __init__(self):
        self.plotter = Plotter()

    def polynomial_input(self):
        print("Polynomial function: ax^n + bx^(n-1) + ...")
        return input("Input function (e.g. x**2 + 2*x + 1): ")

    def trig_input(self):
        print("Trigonometric functions")
        print("Example: sin(x), cos(x), sin(x)+cos(x)")
        return input("Input function: ")

    def custom_input(self):
        print("User-defined functions (sin, cos, exp, log, etc.)")
        return input("Input function: ")

    def run_plot(self, expressions):
        try:
            x_min = float(input("x Minimum value (default -10): ") or -10)
            x_max = float(input("x Maximum value (default 10): ") or 10)
        except:
            x_min, x_max = -10, 10

        save_choice = input("Save image? (y/n): ")

        functions = [Function(expr) for expr in expressions]

        self.plotter.plot(
            functions,
            x_min,
            x_max,
            save=True if save_choice.lower() == "y" else False
        )

    def main_menu(self):
        print("\nFunction Graph Visualization System")
        print("1. Polynomial function")
        print("2. Trigonometric function")
        print("3. Custom function")
        print("4. Multiple functions plotting")
        print("0. Exit")

        choice = input("Please select: ")

        if choice == "1":
            func = self.polynomial_input()
            self.run_plot([func])

        elif choice == "2":
            func = self.trig_input()
            self.run_plot([func])

        elif choice == "3":
            func = self.custom_input()
            self.run_plot([func])

        elif choice == "4":
            funcs = input("Enter multiple functions (separated by commas): ")
            func_list = [f.strip() for f in funcs.split(",")]
            self.run_plot(func_list)

        elif choice == "0":
            print("Exit Program")
            return False

        else:
            print("Invalid choice")

        return True


ui = UserInterface()

while True:
    if not ui.main_menu():
        break