package JSON;

public abstract class JsonElement {

	
	public boolean isJsonObject() {
		return this instanceof JsonObject;
	}
	
	public boolean isJsonArray() {
		return this instanceof JsonArray;
	}
	
	public boolean isJsonPrimitive() {
		return this instanceof JsonPrimitive;
	}
	
	public boolean isJsonNull() {
		return this instanceof JsonNull;
	}
}
