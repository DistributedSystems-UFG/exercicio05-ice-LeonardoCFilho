module Demo
{
    interface Printer
    { // Compatibilidade com o ex.6
        string printString(string s);

        // Novo
        string printUpperCase(string s);
    }
    
    // Novo
    interface Calculator
    {
        int soma(int a, int b);
        int subtrair(int a, int b);
        int multiplicar(int a, int b);
    }
}
