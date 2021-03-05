package jacob.daniel.jdsecuritysolutions;

//Course: CENG319
//Team: JD Security Solutions
//Author: Jacob Arsenault N01244276

import android.content.Context;
import android.content.SharedPreferences;
import android.content.res.Configuration;
import android.os.Bundle;
import android.os.Environment;
import android.util.Log;
import android.widget.SeekBar;
import android.widget.TextView;
import android.widget.VideoView;

import androidx.annotation.NonNull;

import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.storage.FileDownloadTask;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.ListResult;
import com.google.firebase.storage.StorageReference;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;


public class ViewerDevice extends BottomNavigationInflater {

    File dataFile;
    String roomName;
    VideoView screen;
    SeekBar seek;
    SharedPreferences userInfo;
    String username;
    TextView roomTitle;
    TextView data;
    static boolean stop = false;
    ExecutorService executor;


    @Override
    public void onBackPressed() {
        super.onBackPressed();
        this.stop = true;
        executor.shutdownNow();
        finish();
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        this.roomName = getIntent().getExtras().getString("roomname");
        Configuration orientation = getResources().getConfiguration();
        onConfigurationChanged(orientation);

        userInfo = getSharedPreferences("USER_PREF", Context.MODE_PRIVATE);
        username = userInfo.getString("User", "username");
        roomTitle = findViewById(R.id.RoomNameLabel);

        roomTitle.setText(this.roomName);
        fillData();

        //set seekbar listener
        seek = findViewById(R.id.videoProgress);
        seek.setMax(100);
        seek.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {
                int progress = seek.getProgress();
                setVideoFromProgress(progress);
            }
            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {}

            @Override
            public void onProgressChanged(SeekBar seekBar, int progress,boolean fromUser) {

            }
        });

        screen = findViewById(R.id.recordedVideo);

        //create threads to update seekbar in the background as well as play video
        executor = Executors.newFixedThreadPool(2);
        Callable<Boolean> mediaPlayer = new JDMediaPlayer(this, screen, username, roomName);
        Log.println(Log.INFO, "ViewerDevice", "Starting MediaPlayer Thread");
        Future<Boolean> future = executor.submit(mediaPlayer);
        if(future.isDone()){
            Log.println(Log.INFO, "JDMediaPlayer", "No More Content to Play");
        }

        Runnable updater = new SeekBarUpdater();
        executor.submit(updater);
    }

    //update the seekbar based on current index
    class SeekBarUpdater implements Runnable {
        int progress;
        @Override
        public void run() {
            while(!stop){
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                if(JDMediaPlayer.vidIndex==0){
                    progress=0;
                }
                else{
                    progress = (int)(((float)JDMediaPlayer.vidIndex/(float)JDMediaPlayer.vidCount)*100);
                }
                Log.println(Log.INFO, "JDMediaPlayer", "Progress runnable: "+progress);
                seek.setProgress(progress);
            }
        }
    }

    @Override
    public void onConfigurationChanged(Configuration newConfig) {
        super.onConfigurationChanged(newConfig);

        // Checks the orientation of the screen
        if (newConfig.orientation == Configuration.ORIENTATION_PORTRAIT) {
            setContentView(R.layout.viewer_device);
            super.createNavListener();
        }
        else if (newConfig.orientation == Configuration.ORIENTATION_LANDSCAPE) {
            setContentView(R.layout.viewer_device_landscape);
            super.createNavListener();
        }
    }

    public void setVideoFromProgress(int progress){
        Log.println(Log.INFO, "ViewerDevice", "Progress: "+progress);
        JDMediaPlayer.vidIndex = (int) (Math.round((JDMediaPlayer.vidCount * progress)/100))-1;
        Log.println(Log.INFO, "ViewerDevice", "Index: "+JDMediaPlayer.vidIndex+" Count: "+JDMediaPlayer.vidCount);
    }

    public void fillData(){
        String filePath = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DCIM) + File.separator+"roomData.txt";
        dataFile = new File(filePath);
        FirebaseStorage fbInstance;
        StorageReference dataRef;
        fbInstance = FirebaseStorage.getInstance();;
        dataRef = fbInstance.getReference().child(username+ File.separator+roomName +File.separator+"temp.txt");
        Log.println(Log.INFO, "Firebase", "References Made For Data Retrieval");

        dataRef.getFile(dataFile)
                .addOnSuccessListener(new OnSuccessListener<FileDownloadTask.TaskSnapshot>() {
                    @Override
                    public void onSuccess(FileDownloadTask.TaskSnapshot taskSnapshot) {
                        StringBuilder text = new StringBuilder();

                        try {
                            BufferedReader br = new BufferedReader(new FileReader(dataFile));
                            String line;
                            int i = 0;
                            while ((line = br.readLine()) != null) {

                                if(i<7) {
                                    i++;
                                    text.append(line);
                                    text.append('\n');
                                }
                            }
                            br.close();
                        }
                        catch (FileNotFoundException e) {
                            //You'll need to add proper error handling here
                        } catch (IOException e) {
                            e.printStackTrace();
                        }

                        data = (TextView)findViewById(R.id.DataLabel);

                        data.setText(text.toString());
                    }
                }).addOnFailureListener(new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception exception) {
                    Log.println(Log.INFO, "Firebase", "Error getting room data.");
                }
        });
    }
}