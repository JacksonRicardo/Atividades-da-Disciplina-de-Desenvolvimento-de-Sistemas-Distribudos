struct numbers{
	int a;
	int b;
};

program ADD_PROG{
	version ADD_VERS{
		int soma (numbers) = 1;
		int resto (numbers) = 2;
		int divisao (numbers) = 3;
		int multiplicacao (numbers) = 4;
		int sair (numbers) = 5;	
	} = 1;
} = 0x23451111;
