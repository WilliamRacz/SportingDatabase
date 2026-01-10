import java.nio.file.*;
import java.util.*;

public class env {
    private static final Map<String, String> vars = new HashMap<>();

    public static void load() {
        try {
            List<String> lines = Files.readAllLines(Path.of(".env"));
            for (String line : lines) {
                if (line.contains("=")) {
                    String[] parts = line.split("=", 2);
                    vars.put(parts[0].trim(), parts[1].trim());
                }
            }
        } catch (Exception e) {
        }
    }

    public static String get(String key) {
        return vars.getOrDefault(key, System.getenv(key));
    }
}