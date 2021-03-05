package jacob.daniel.jdsecuritysolutions;

//Course: CENG319
//Team: JD Security Solutions
//Author: Jacob Arsenault N01244276

import android.content.Intent;
import android.content.res.Configuration;
import android.os.Bundle;
import android.view.MenuItem;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.google.android.material.bottomnavigation.BottomNavigationView;

public abstract class BottomNavigationInflater extends AppCompatActivity {
    private BottomNavigationView bottomNavigationView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    protected void createNavListener(){
        BottomNavigationView bottomNavigationView;
        bottomNavigationView = (BottomNavigationView)findViewById(R.id.navigationView);
        if(bottomNavigationView != null) {
            bottomNavigationView.setOnNavigationItemSelectedListener(new BottomNavigationView.OnNavigationItemSelectedListener() {
                @Override
                public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                    Intent intent;
                    switch (item.getItemId()){
                        case R.id.menu_home:
                            intent = new Intent(getBaseContext(), ChooseConfig.class);
                            finish();
                            startActivity(intent);
                            break;
                        case R.id.menu_settings:
                            intent = new Intent(getBaseContext(), Settings.class);
                            finish();
                            startActivity(intent);
                            break;
                        case R.id.menu_viewer:
                            intent = new Intent(getBaseContext(), ViewerMenu.class);
                            finish();
                            startActivity(intent);
                            break;
                        case R.id.menu_recorder:
                            intent = new Intent(getBaseContext(), CameraDevice.class);
                            finish();
                            startActivity(intent);
                            break;
                    }
                    return false;
                }
            });
        }
    }
    @Override
    public void onConfigurationChanged(Configuration newConfig) {
        super.onConfigurationChanged(newConfig);
    }

}
