package org.samples;

import java.util.ArrayList;
import java.util.List;

public class Line {
    private List<Part> parts;

    public Line() {
        this.parts = new ArrayList<>();
    }

    public static Line keep(String text) {
        Line line = new Line();
        line.parts.add(new Part(text, "unchanged"));
        return line;
    }

    public Line remove(String text) {
        this.parts.add(new Part(text, "removed"));
        return this;
    }

    public Line add(String text) {
        this.parts.add(new Part(text, "added"));
        return this;
    }

    public Line keepPart(String text) {
        this.parts.add(new Part(text, "unchanged"));
        return this;
    }

    public List<Part> getParts() {
        return parts;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < parts.size(); i++) {
            sb.append(parts.get(i).toString());
            if (i < parts.size() - 1) {
                sb.append(", ");
            }
        }
        return sb.toString();
    }
}

