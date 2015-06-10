package com.cs419_group18.corvallisreuseandrepairdirectory;

import android.app.ProgressDialog;
import android.content.Intent;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.JsonHttpResponseHandler;

import org.apache.http.Header;
import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;


public class ReuseItemActivity extends ActionBarActivity implements AdapterView.OnItemClickListener {
    Intent intent;
    private static final String BASE_URL = "http://52.26.111.76:8000/crrd/";
    AsyncHttpClient client = new AsyncHttpClient();
    ListView itemListView;
    static ArrayList<String> itemList;
    static ArrayList<String> itemIDs;
    static ArrayAdapter itemAdapter;
    String pk;      //DB primary key
    ProgressDialog progDialog;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_reuse_item);

        // set up the arrayList and adapter that will populate the item ListView
        itemListView = (ListView) findViewById(R.id.listview_reuseItem);
        itemList = new ArrayList<>();
        itemIDs = new ArrayList<>();
        itemAdapter = new ArrayAdapter(this, R.layout.crrd_list_item, itemList);
        itemListView.setAdapter(itemAdapter);
        itemListView.setOnItemClickListener(this);

        pk = this.getIntent().getExtras().getString("pk");

        progDialog = new ProgressDialog(this);
        progDialog.setMessage("Fetching data");
        progDialog.setCancelable(false);

        progDialog.show();

        // perform GET to do initial fill of the item listview
        client.get(BASE_URL + pk + "/useitems/", new JsonHttpResponseHandler() {
            @Override
            public void onSuccess(int statusCode, Header[] headers, JSONArray response) {
                progDialog.dismiss();
                JSONObject item, fields;
                for (int i = 0; i < response.length(); ++i) {
                    try {
                        item = response.getJSONObject(i);
                        fields = item.getJSONObject("fields");
                        itemList.add(fields.getString("itemName"));
                        itemIDs.add(item.getString("pk"));
                    } catch (Exception ex) {
                        Log.d("jh json exception", ex.getMessage());
                    }
                }
                itemAdapter.notifyDataSetChanged();
            }

            @Override
            public void onFailure(int statusCode, Header[] headers, String responseString, Throwable error) {
                progDialog.dismiss();
                Log.d("jh item GET fail", responseString);
            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_reuse_cat, menu);
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
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        intent = new Intent(this, ReuseBizActivity.class);
        intent.putExtra("pk", itemIDs.get(position));
        startActivity(intent);
    }
}
