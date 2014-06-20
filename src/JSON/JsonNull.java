package JSON;

public class JsonNull extends JsonElement {
	
	private static JsonNull instance;

	public JsonNull() {}
	
	public static JsonNull getInstance() {
		if(instance == null) 
			instance = new JsonNull();
		return instance;
	}
	
	public String toString() {
		return "null";
	}
	
	public int hashCode() {
		return JsonNull.class.hashCode();
	}
	
	public boolean equals(Object other) {
		return this == other || other instanceof JsonNull;
	}
}