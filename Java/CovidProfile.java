public class CovidProfile {
    // public static int all_object = 0;
    // public static int all_death = 0;
    private String date;
    private String loc;
    private int accumulatedCases;
    private int curedCases;
    private int deathCases;

    public CovidProfile() {
        this.date = "none";
        this.loc = "none";
        this.accumulatedCases = 0;
        this.curedCases = 0;
        this.deathCases = 0;
        // this.all_object++;
    }

    public CovidProfile(String date, String loc, int accumulatedCases, int curedCases, int deathCases) {
        this.date = date;
        this.loc = loc;
        this.accumulatedCases = accumulatedCases;
        this.curedCases = curedCases;
        this.deathCases = deathCases;
        // this.all_object++;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getLocation() {
        return loc;
    }

    public void setLocation(String loc) {
        this.loc = loc;
    }

    public int getACCCases() {
        return accumulatedCases;
    }

    public void setACCCases(int noACC) {
        this.accumulatedCases = noACC;
    }

    public int getCuredCases() {
        return curedCases;
    }

    public void setCuredCases(int noCured) {
        this.curedCases = noCured;
    }

    public int getDeathCases() {
        return deathCases;
    }

    public void setDeathCases(int noDeath) {
        this.deathCases = noDeath;
        // all_death = noDeath;
    }

    public void printPatientInfo() {
        System.out.println(loc + " at " + date);
        System.out.println("Accumulative Patient: " + accumulatedCases);
        System.out.println("Cured Patient: " + curedCases);
        System.out.println("Death Case: " + deathCases);
    }

    // public void boolean isSevere() {
    // if (all_death > 10000) {
    // return true;
    // }
    // }
}
