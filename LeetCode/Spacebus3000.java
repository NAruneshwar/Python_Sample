// Aruneshwar Nalluri
// Spacebus3000 submission


import java.util.*;
import java.io.*;

class Spacebus3000 {
    public static void main(String[] args) { 
        // Initiating an ArrayList of Islands which are connected among themselves
        ArrayList<HashSet<String>> islandList = formIslands(args);
        boolean flag = false;
        try{
            for(HashSet<String> connectedSet : islandList){
                // Iterating through the connected nodes inside and Island
                if (connectedSet.contains(args[1]) && (connectedSet.contains(args[2]))){
                    flag = true;
                    System.out.println("yes");
                }
            }
            if(flag==false){
                // if both of the elements dont exist or dont exist on same island
                System.out.println("no");
            }
        }
        catch(Exception e){
            System.out.println("Invalid arguments passed please check and try again");
        }
    }

    public static ArrayList<HashSet<String>> formIslands(String[] args){
        // Function to grab the file, parse it through and convert it to our desired datastructure.
        ArrayList<HashSet<String>> islandList = new ArrayList<HashSet<String>>();
        try{  
            File file=new File(args[0]);   
            FileReader fr=new FileReader(file);  
            BufferedReader br=new BufferedReader(fr); 
            String line;  
            while((line=br.readLine())!=null)  
            {   // go through each line as an entry from file
                boolean flag = true;
                String [] stations = line.split(",",2);
                stations[0] = stations[0].trim();
                stations[1] = stations[1].trim();
                HashSet<String> oldSet = new HashSet<>();
                for(HashSet<String> connectedSet : islandList){
                    // Iterate through existing network to check if its part of any
                    if (connectedSet.contains(stations[0]) || connectedSet.contains(stations[1])){
                        if(flag==false){
                            // if its connecting two islands we combine them
                            connectedSet.addAll(oldSet);
                            oldSet.clear();
                        }
                        connectedSet.add(stations[0]);
                        connectedSet.add(stations[1]);
                        flag = false;
                        oldSet = connectedSet;
                    }
                }
                if (flag){
                    // if its new island we create a new network and add it to array
                    HashSet<String> newentry = new HashSet<>();
                    newentry.add(stations[0]);
                    newentry.add(stations[1]);
                    islandList.add(newentry);
                }  
        }  
            fr.close();    //closes the stream and release the resources  
        }  
        catch(IOException e)
        {  
            System.out.println("Please check file name again and retry"); 
        }
        return islandList;
    }
}