package JSON;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class JsonArray extends JsonElement {
	
	private List<JsonElement> list = new ArrayList<JsonElement>();

	protected List<JsonElement> getList() {
		return list;
	}
	
	public void add(JsonElement element) {
		JsonElement item = element;
		if(element == null)
			item = JsonNull.getInstance();
		list.add(item);
	}
	
	public JsonElement get(int i) {
		return list.get(i);
	}
	
	public int size() {
		return list.size();
	}
	
	// TO STRING
	
	public String toString() {
		StringBuffer sb = new StringBuffer();
		sb.append('[');
		boolean first = true;
		for (JsonElement element : list) {
			if (first) {
				first = false;
			} else {
				sb.append(',');
				sb.append("\n");
			}
			sb.append(element.toString());
		}
		sb.append(']');
		return sb.toString();
	}
	
	// EQUALS AND HASHCODE
	
	public int hashCode() {
		return list.hashCode();
	}
	
	public boolean equals(Object other) {
		if(other == null)
			return false;
		try {
			return this.list.equals(((JsonArray)other).getList());
		} catch(ClassCastException e) {
			return false;
		}
	}

}
