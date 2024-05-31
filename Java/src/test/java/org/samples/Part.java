package org.samples;

public class Part {
    private String text;
    private String status;

    public Part(String text, String status) {
        this.text = text;
        this.status = status;
    }

    public boolean isUnchanged() {
        return "unchanged".equals(status);
    }

    public boolean isRemoved() {
        return "removed".equals(status);
    }

    public boolean isAdded() {
        return "added".equals(status);
    }

    @Override
    public String toString() {
        return "`" + text + "`[" + status + "]";
    }
}

