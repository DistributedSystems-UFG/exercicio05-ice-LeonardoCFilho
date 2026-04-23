module Demo
{
    interface Printer
    {
        void printString(string s);

        // Novo
        void printUpperCase(string s);
    }
    
    // Novo
    interface Calculator
    {
        int soma(int a, int b);
        int subtrair(int a, int b);
        int multiplicar(int a, int b);
    }
}
