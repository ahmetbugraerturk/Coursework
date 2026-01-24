from q1a import approximate_square_root

def find_polynomial_roots(a, b, c, epsilon=1e-7, max_iterations=1000):
        """
        Finds roots of the polynomial a*x^2 + b*x + c = 0
        """
        if a == 0:
            if b == 0:
                return None
            else:
                return (-c/b,)
        else:
            disc = approximate_square_root((b**2-4*a*c), epsilon, max_iterations)
            if disc == None:
                return None
            elif disc < 0:
                return None
            else:
                return (-b+disc)/(2*a), (-b-disc)/(2*a)
            