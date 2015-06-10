package com.cs419_group18.corvallisreuseandrepairdirectory;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.ActionBarActivity;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.TextView;

import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.MapFragment;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;


public class ReuseBizDetailActivity extends ActionBarActivity implements OnMapReadyCallback {
    TextView bizNameTextView;
    TextView bizAddressTextView;
    TextView bizCityTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_reuse_biz_detail);

        bizNameTextView = (TextView) findViewById(R.id.reuseBizName);
        bizAddressTextView = (TextView) findViewById(R.id.reuseBizAddress);
        bizCityTextView = (TextView) findViewById(R.id.reuseBizCity);

        bizNameTextView.setText("XYZ Business");
        bizAddressTextView.setText("21 Jump St.");
        bizCityTextView.setText("Corvallis");

        MapFragment mapFragment = (MapFragment) getFragmentManager().findFragmentById(R.id.reuseMap);
        mapFragment.getMapAsync(this);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_reuse_biz_detail, menu);
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
        map.addMarker(new MarkerOptions()
                .position(new LatLng(44.559,-123.265))
                .title("Corvallis Area"));
        map.setOnMapClickListener(new GoogleMap.OnMapClickListener() {
            @Override
            public void onMapClick(LatLng latLng) {
                startActivity(new Intent(ReuseBizDetailActivity.this, ReuseMapActivity.class));
            }
        });
    }
}
