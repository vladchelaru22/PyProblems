class Image():
    def __init__(self, format='P3', rows=0, columns=0, max_value=255, pixels=[[]]):
        self.format = format
        self.rows = rows
        self.columns = columns
        self.max_value = max_value
        self.pixels = pixels
    def __str__(self):
        # use this for debugging
        image = ""
        image += f"{self.format}{self.rows} {self.columns}\n{self.max_value}\n"
        for i in range(self.rows):
            for j in range(3 * self.columns):
                image += f"{self.pixels[i][j]} "
            image += "\n"
        return image
    def sepia(self):
        # apply sepia filter to the image
        for i in range(0,self.rows):
            for j in range(0,self.columns*3,3):
                r = self.pixels[i][j]
                g = self.pixels[i][j+1]
                b = self.pixels[i][j+2]

                sepia_r = int(0.393*r + 0.769*g + 0.189*b)
                sepia_g = int(0.349*r + 0.686*g + 0.168*b)
                sepia_b = int(0.272*r + 0.534*g + 0.131*b)

                if sepia_r > 255:
                    sepia_r = 255

                if sepia_g>255:
                    sepia_g = 255

                if sepia_b>255:
                    sepia_b = 255
                    
                self.pixels[i][j] = sepia_r
                self.pixels[i][j+1] = sepia_g
                self.pixels[i][j+2] = sepia_b

    def read(self, filename):
        # read from file and assign the correct parameters (see README and input examples)
        f = open(filename,'r')
        self.format = f.readline()
        line = f.readline()
        self.rows = int(line[0])
        self.columns = int(line[2])
        line = f.readline()
        self.max_value = int(line)
        self.pixels = [[0, 0, 0] * self.columns for i in range(self.rows)]
        for i in range(self.rows):    
            line = f.readline()
            x = line.split()
            for j in range(3 * self.columns):
                self.pixels[i][j] = int(x[j])
        pass
    
 
    def write(self, filename):
        # write to file in the correct format (see README and input examples)
        f = open(filename,'w')
        f.write(self.format)
        f.write(str(self.rows))
        f.write(' ')
        f.write(str(self.columns))
        f.write("\n")
        f.write(str(self.max_value))
        f.write("\n")
        for i in range(self.rows):
            for j in range(self.columns*3):
                f.write(str(self.pixels[i][j]))
                f.write(' ')
            f.write("\n")
        f.close
        pass


