package JSON;

public class JsonPrimitive extends JsonElement {

	private Object value;

	// CONSTRUCTORS

	public JsonPrimitive(Boolean bool) {
		this.value = bool;
	}

	public JsonPrimitive(Number num) {
		this.value = num;
	}

	public JsonPrimitive(String str) {
		this.value = str;
	}

	public JsonPrimitive(Character ch) {
		this.value = ch;
	}

	// TO STRING

	public String toString() {
		return value.toString();
	}

	// GET FUNCTIONS

	public Boolean getAsBoolean() {
		return (Boolean) value;
	}

	public Character getAsChar() {
		return (Character) value;
	}

	public String getAsString() {
		return (String) value;
	}

	public Float getAsFloat() {
		return ((Number) value).floatValue();
	}

	public Integer getAsInt() {
		return ((Number) value).intValue();
	}

	public Long getAsLong() {
		return ((Number) value).longValue();
	}

	// EQUALS AND HASHCODE

	public int hashCode() {
		return value.hashCode();
	}

	public boolean equals(Object other) {
		if (other == null)
			return false;
		try {
			if (this.value == null)
				return ((JsonPrimitive) other).value == null;

			return this.value.equals(((JsonPrimitive) other).getValue());
		} catch (ClassCastException e) {
			return false;
		}
	}

	protected Object getValue() {
		return value;
	}
}
