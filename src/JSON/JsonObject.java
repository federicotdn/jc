package JSON;

import java.util.LinkedHashMap;
import java.util.Map;

public class JsonObject extends JsonElement {

	private Map<String, JsonElement> map = new LinkedHashMap<String, JsonElement>();

	public void add(String name, JsonElement element) {
		map.put(name, element);
	}

	public JsonElement get(String name) {
		return map.get(name);
	}

	public void addProperty(String name, Boolean value) {
		map.put(name, new JsonPrimitive(value));
	}

	public String toString() {
		StringBuffer sb = new StringBuffer();
		sb.append('{');
		boolean first = true;
		for (Map.Entry<String, JsonElement> entry : map.entrySet()) {
			if (first) {
				first = false;
			} else {
				sb.append(',');
			}
			sb.append('\"');
			sb.append(entry.getKey());
			sb.append("\":");
			JsonElement elem = entry.getValue();
			if(elem instanceof JsonPrimitive)
				sb.append("\"");
			sb.append(elem.toString());
			if(elem instanceof JsonPrimitive)
				sb.append("\"");
		}
		sb.append('}');
		return sb.toString();
	}
}
