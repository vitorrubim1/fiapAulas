package While;

public class Exercise39 {

	public static void main(String[] args) {
		int index = 1, t1 = -1, t2 = 1, t3 = 0;

		while (index < 31) {	
			t3 = t1 + t2;
			t1 = t2;
			t2 = t3;
			
			index = index + 1;
			System.out.printf("\n%d", t3);
		}
		System.out.println("\nFim");
	}

}
