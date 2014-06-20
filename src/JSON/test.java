package JSON;

public class test {


	public static void main(String[] args) {
		JsonArray array1 = new JsonArray();
		
		JsonObject obj1 = new JsonObject();
		obj1.add("name", new JsonPrimitive("Javier Fraire"));
		obj1.add("id", new JsonPrimitive(1));
		
		JsonObject obj2 = new JsonObject();
		obj2.add("name", new JsonPrimitive("Federico Tedin"));
		obj2.add("id", new JsonPrimitive(2));
		
		JsonObject obj3 = new JsonObject();
		obj3.add("name", new JsonPrimitive("Iñaki Lanusse"));
		obj3.add("id", new JsonPrimitive(3));
		
		JsonObject obj4 = new JsonObject();
		obj4.add("name", new JsonPrimitive("Agustina Fainguersch"));
		obj4.add("id", new JsonPrimitive(4));
		
		JsonObject nullObj = new JsonObject();
		nullObj.add("name", new JsonNull());
		nullObj.add("id", new JsonNull());
		
		array1.add(obj1);
		array1.add(obj2);
		array1.add(obj3);
		array1.add(obj4);
		array1.add(nullObj);
		
		System.out.println(array1);

	}

}
