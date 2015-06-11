package com.cs419_group18.corvallisreuseandrepairdirectory;

import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;

import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.MapFragment;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;


public class RepairMapActivity extends ActionBarActivity implements OnMapReadyCallback {
    double lat;
    double lng;
    String name;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_repair_map);

        MapFragment mapFragment = (MapFragment) getFragmentManager().findFragmentById(R.id.repairMap);
        mapFragment.getMapAsync(this);

        lat = this.getIntent().getExtras().getDouble("lat");
        lng = this.getIntent().getExtras().getDouble("lng");
        name = this.getIntent().getExtras().getString("name");
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_repair_map, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @Override
    public void onMapReady(GoogleMap map) {
        if (lat != 0 && lng != 0) {
            map.addMarker(new MarkerOptions()
                    .position(new LatLng(lat, lng))
                    .title(name));
        }
    }
}
