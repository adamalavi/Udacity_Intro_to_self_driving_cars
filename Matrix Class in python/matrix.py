import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        # TODO - your code here
        elif (self.h == 1):
            self.determinant = self.g[0][0]
        elif (self.h == 2):
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            
            self.determinant = a*d - b*c
            
        return self.determinant
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        self.trace = 0
        for i in range(self.h):
            self.trace += self.g[i][i]
        
        return self.trace
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        inverse = []
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        elif(self.h == 1):
            inverse.append([1/self.g[0][0]])
            return Matrix(inverse)
        elif(self.h == 2):
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            factor = a*d-b*c
            if factor == 0:
                raise ValueError('The given matrix is non-invertible')
            else:
                inverse = Matrix([[d/factor, -b/factor], [-c/factor, a/factor]])
                return inverse
                
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_t = []
        for i in range(self.w):
            row = []
            for j in range(self.h):
                row.append(self.g[j][i])
            matrix_t.append(row)
            
        return Matrix(matrix_t)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        matrixSum = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] + other.g[i][j])
            matrixSum.append(row)
        add = Matrix(matrixSum)
       
        return add

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        matrix_neg = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(-(self.g[i][j]))
            matrix_neg.append(row)
        neg_val = Matrix(matrix_neg)
        
        return neg_val
    
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        matrixDiff = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] - other.g[i][j])
            matrixDiff.append(row)
        diff = Matrix(matrixDiff)
        return diff
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        product = []
        transposeB = other.T()

        for r1 in range(self.h):
            new_row = []
            for r2 in range(transposeB.h):
                # Calculate the dot product between each row of matrix A
                # with each row in the transpose of matrix B
                result = 0
                for i in range(len(self.g[r1])):
                    result += self.g[r1][i] * transposeB.g[r2][i]
                new_row.append(result)
            # Store the results in the product variable
            product.append(new_row)
        
        prod = Matrix(product)
        return prod
    
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            
            #   
            # TODO - your code here
            #
            res = []
            for i in range(self.h):
                new_row = []
                for j in range(self.w):
                    new_row.append(other * self.g[i][j])
                res.append(new_row)
            scalar_mult = Matrix(res)
        return scalar_mult 
                    