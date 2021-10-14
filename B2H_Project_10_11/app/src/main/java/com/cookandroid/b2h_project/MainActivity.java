package com.cookandroid.b2h_project;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.content.pm.ActivityInfo;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;

import android.graphics.Picture;
import android.graphics.PixelFormat;
import android.hardware.Camera;
import android.os.Build;
import android.os.Environment;
import android.provider.MediaStore;
import android.os.Bundle;
import android.Manifest;
import android.os.Handler;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import android.speech.tts.TextToSpeech;
import static android.speech.tts.TextToSpeech.ERROR;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;


public class MainActivity extends AppCompatActivity implements View.OnClickListener, SurfaceHolder.Callback, Runnable {

    private Context mContext = this;
    Camera camera = null;
    SurfaceView sv;
    SurfaceHolder surfaceHolder;
    boolean previewing = false;
    LayoutInflater controlInflator = null;

    Button connect_btn, camera_on, camera_picture, camera_delete, Trans_btn, tts_btn, reset_btn, file_btn;
    EditText ip_edit;               // ip 에디트
    TextView show_text;             // 서버에서온거 보여주는 에디트
    // 소켓통신에 필요한것
    private String html = "";
    private Handler mHandler;

    private Socket socket;

    private BufferedReader networkReader;
    private PrintWriter networkWriter;

    private DataOutputStream dos;
    private DataInputStream dis;
    private DataOutputStream dos_1;
    private DataInputStream dis_1;


    private String ip = "121.185.14.241";            // IP 번호
    private int port = 9980;// port 번호
    private String msg;

    private TextToSpeech tts;
    private String line = "";
    private int count = 0;
    private String dirName = "/MyCameraApp";
    private int I_count = 1;





    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT); //세로 고정

        connect_btn = (Button)findViewById(R.id.connect_btn);
        camera_on=(Button)findViewById(R.id.camera_on);
        camera_picture=(Button)findViewById(R.id.camera_picture);
        camera_delete=(Button)findViewById(R.id.camera_delete);
        Trans_btn=(Button)findViewById(R.id.Trans_btn);
        tts_btn=(Button)findViewById(R.id.tts_btn);
        reset_btn=(Button)findViewById(R.id.reset_btn);
        file_btn=(Button)findViewById(R.id.file_btn);

        connect_btn.setOnClickListener(this);
        camera_on.setOnClickListener(this);
        camera_picture.setOnClickListener(this);
        camera_delete.setOnClickListener(this);
        Trans_btn.setOnClickListener(this);
        tts_btn.setOnClickListener(this);
        reset_btn.setOnClickListener(this);
        file_btn.setOnClickListener(this);


        ip_edit = (EditText)findViewById(R.id.ip_edit);
        show_text = (TextView)findViewById(R.id.show_text);

        getWindow().setFormat(PixelFormat.UNKNOWN);
        sv=(SurfaceView)findViewById(R.id.sv);
        surfaceHolder = sv.getHolder();
        surfaceHolder.addCallback(this);
        surfaceHolder.setType(SurfaceHolder.SURFACE_TYPE_PUSH_BUFFERS);

        controlInflator = LayoutInflater.from(getBaseContext());
        View viewControl = controlInflator.inflate(R.layout.control, null);
        ViewGroup.LayoutParams layoutParamsControl=new ViewGroup.LayoutParams(ViewGroup.LayoutParams.FILL_PARENT, ViewGroup.LayoutParams.FILL_PARENT);
        this.addContentView(viewControl, layoutParamsControl);


        //동적퍼미션 작업
        if(Build.VERSION.SDK_INT>=Build.VERSION_CODES.M){
            int permissionResult= checkSelfPermission(Manifest.permission.CAMERA);
            if(permissionResult== PackageManager.PERMISSION_DENIED){
                String[] permissions= new String[]{Manifest.permission.CAMERA, Manifest.permission.WRITE_EXTERNAL_STORAGE};
                requestPermissions(permissions,10);
            }
        }else{
            sv.setVisibility(View.VISIBLE);
        }



        



        tts = new TextToSpeech(this, new TextToSpeech.OnInitListener() {
            public void onInit(int status) {
                if (status != ERROR) {
                    tts.setLanguage(Locale.KOREA);
                }
            }
        });


    }

    @Override
    public void onClick(View v) {
        switch(v.getId()){
            case R.id.connect_btn:     // ip 받아오는 버튼
                connect();
                break;
            case R.id.camera_on:
                camera_open();
                break;
            case R.id.camera_picture:
                take_picture();
                break;
            case R.id.camera_delete:
                setDirEmpty(dirName);
                break;
            case R.id.Trans_btn:
                Trans();
                break;
            case R.id.tts_btn:
                TTS();
                break;
            case R.id.file_btn:
                connect_1();
                break;
            case R.id.reset_btn:
                reset();
                break;

        }
    }

    @Override
    public void run() {

    }

    void connect() {
        mHandler = new Handler();
        Log.w("connect", "연결 하는중");
        // 받아오는거
        Thread checkUpdate = new Thread() {
            public void run() {
                // ip받기
                String newip = String.valueOf(ip_edit.getText());

                // 서버 접속
                try {
                    socket = new Socket(newip, port);
                    Log.w("서버 접속됨", "서버 접속됨");   // 토스트메시지로 연결됐다고 띄워야됨 로그는 피시에서만 확인
                } catch (IOException e1) {
                    Log.w("서버접속못함", "서버접속못함");
                    e1.printStackTrace();
                }

                Log.w("edit 넘어가야 할 값 : ", "안드로이드에서 서버로 연결요청");

                try {
                    dos = new DataOutputStream(socket.getOutputStream());   // output에 보낼꺼 넣음
                    dis = new DataInputStream(socket.getInputStream());     // input에 받을꺼 넣어짐
                    dos.writeUTF("안드로이드에서 서버로 연결요청");

                } catch (IOException e) {
                    e.printStackTrace();
                    Log.w("버퍼", "버퍼생성 잘못됨");
                }
                Log.w("버퍼", "버퍼생성 잘됨");


            }
        };
        // 소켓 접속 시도, 버퍼생성
        checkUpdate.start();
    }


    // 로그인 정보 db에 넣어주고 연결시켜야 함.
    void connect_1(){
        mHandler = new Handler();
        Log.w("connect","연결 하는중");
        // 받아오는거
        Thread checkUpdate = new Thread() {
            public void run() {
                // ip받기
                String newip = String.valueOf(ip_edit.getText());


                // 서버 접속
                for (int i = 1; i < I_count; i++) {
                    try {
                        socket = new Socket(newip, port);
                        Log.w("서버 접속됨", "서버 접속됨");   // 토스트메시지로 연결됐다고 띄워야됨 로그는 피시에서만 확인
                    } catch (IOException e1) {
                        Log.w("서버접속못함", "서버접속못함");
                        e1.printStackTrace();
                    }

                    Log.w("edit 넘어가야 할 값 : ", "안드로이드에서 서버로 연결요청");

                    String Filename = Integer.toString(i);
                    String path = Environment.getExternalStoragePublicDirectory(
                            Environment.DIRECTORY_PICTURES).toString() + dirName;
                    try {

                        PrintWriter out = new PrintWriter(new BufferedWriter(new
                                OutputStreamWriter(socket.getOutputStream())), true);
                        DataInputStream dis = new DataInputStream(new
                                FileInputStream(new File(path, Filename + ".jpg"))); //읽을 파일 경로 적어 주시면 됩니다.
                        DataOutputStream dos = new
                                DataOutputStream(socket.getOutputStream());
                        byte[] buf = new byte[1024];

                        while (dis.read(buf) > 0) { //길이 정해주고 딱 맞게 서버로 보냅니다.
                            dos.write(buf);
                            dos.flush();
                        }
                        dos.close();
                    } catch (Exception e) {
                        e.printStackTrace();
                    }

                }
            }

                /*try {
                    dos_1 = new DataOutputStream(socket.getOutputStream());   // output에 보낼꺼 넣음
                    dis_1 = new DataInputStream(socket.getInputStream());     // input에 받을꺼 넣어짐
                    dos_1.writeUTF("안드로이드에서 서버로 연결요청");

                } catch (IOException e) {
                    e.printStackTrace();
                    Log.w("버퍼", "버퍼생성 잘못됨");
                }
                Log.w("버퍼","버퍼생성 잘됨");*/





        };
        // 소켓 접속 시도, 버퍼생성
        checkUpdate.start();
    }


    void Trans(){



        mHandler = new Handler();
        Thread checkUpdate = new Thread() {
            public void run() {
                    // 서버에서 받아옴
                if (count == 0) { //게속 버퍼에 채우는 것을 방지
                    try {
                        byte[] receiver = null;
                        receiver = new byte[1024];
                        dis.read(receiver);
                        line = new String(receiver);

                        //line = (String) dis.readUTF();
                        show_text.setText(line);
                        count = 1;

                    } catch (Exception e) {

                    }
                }
            }
        };
        checkUpdate.start();
    }


    void reset(){
        mHandler = new Handler();

        Thread checkUpdate = new Thread() {

            public void run() {

                line = "";
                show_text.setText(line);
                if (count == 1) { //계속 재요청 하는 것을 방지
                    try {
                        dos = new DataOutputStream(socket.getOutputStream());   // output에 보낼꺼 넣음
                        dis = new DataInputStream(socket.getInputStream());     // input에 받을꺼 넣어짐
                        dos.writeUTF("안드로이드에서 문자열 재요청");
                        count = 0;

                    } catch (IOException e) {
                        e.printStackTrace();
                        Log.w("버퍼", "버퍼생성 잘못됨");
                    }
                    Log.w("버퍼", "버퍼생성 잘됨");
                }
            }
        };
        checkUpdate.start();
    }
    void TTS(){
        mHandler = new Handler();
        Thread checkUpdate = new Thread() {
            public void run() {
                String a = line;
                tts.speak(a.toString(),TextToSpeech.QUEUE_FLUSH, null);
            }
        };
        checkUpdate.start();
        }

    void camera_open(){
        Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);

        if (intent.resolveActivity(getPackageManager()) != null) {
            startActivityForResult(intent, 101);

            if (!previewing) {
                camera = Camera.open();
                if (camera != null) {
                    try {
                        camera.setPreviewDisplay(surfaceHolder);
                        camera.startPreview();
                        previewing = true;

                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }



    void take_picture(){
        camera.takePicture(myShutterCallback,
                myPictureCallback_RW, myPictureCallback_JPG);

    }

    Camera.ShutterCallback myShutterCallback = new Camera.ShutterCallback(){

        @Override
        public void onShutter() {

        }
    };

    Camera.PictureCallback myPictureCallback_RW= new Camera.PictureCallback() {
        @Override
        public void onPictureTaken(byte[] arg0, Camera camera) {

        }
    };

    Camera.PictureCallback myPictureCallback_JPG = new Camera.PictureCallback(){

        @Override
        public void onPictureTaken(byte[] arg0, Camera camera) {
            File pictureFile =getOutputMediaFile(I_count);
            I_count += 1;
            if(pictureFile == null){
                Toast.makeText(mContext, "Error Saving! ",Toast.LENGTH_SHORT).show();
                return;
            }
            try{
                FileOutputStream fos=new FileOutputStream(pictureFile);
                fos.write(arg0);
                fos.close();
                camera.startPreview();

            } catch (FileNotFoundException e) {
                Log.d("Filed is not found",""+e.getMessage() );
                e.printStackTrace();
            } catch (IOException e) {
                Log.d("Error accessing file: ",""+e.getMessage() );
                e.printStackTrace();
            }
            Bitmap bitmapPicture = BitmapFactory.decodeByteArray(arg0, 0, arg0.length);


        }
    };


    @Override
    public void surfaceCreated(SurfaceHolder holder) {
        camera= Camera.open();
        camera.setDisplayOrientation(90);
    }

    @Override
    public void surfaceChanged(SurfaceHolder holder, int format, int width, int height) {
        if(previewing){
            camera.stopPreview();
            previewing=false;
        }

        if(camera != null){
            try{
                camera.setPreviewDisplay(surfaceHolder);
                camera.startPreview();
                previewing=true;
            }catch(IOException e){
                e.printStackTrace();
            }
        }
    }

    @Override
    public void surfaceDestroyed(SurfaceHolder holder) {
        camera.stopPreview();
        camera.release();
        camera=null;
        previewing=false;
    }


    /** 이미지를 저장할 파일 객체를 생성합니다 */
    private static File getOutputMediaFile(int I_count){
        // SD카드가 마운트 되어있는지 먼저 확인해야합니다
        // Environment.getExternalStorageState() 로 마운트 상태 확인 가능합니다

        File mediaStorageDir = new File(Environment.getExternalStoragePublicDirectory(
                Environment.DIRECTORY_PICTURES), "MyCameraApp");
        // 굳이 이 경로로 하지 않아도 되지만 가장 안전한 경로이므로 추천함.

        // 없는 경로라면 따로 생성한다.
        if (! mediaStorageDir.exists()){
            if (! mediaStorageDir.mkdirs()){
                Log.d("MyCamera", "failed to create directory");
                return null;
            }
        }

        // 파일명을 적당히 생성. 여기선 시간으로 파일명 중복을 피한다.
        //String timeStamp = new SimpleDateFormat("yyyyMMdd_HHmmss").format(new Date());
        String FileName =Integer.toString(I_count);

        File mediaFile;


        mediaFile = new File(mediaStorageDir.getPath() + File.separator + FileName  + ".jpg");
        Log.i("MyCamera", "Saved at"+ Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_PICTURES));

        I_count += 1;


        return mediaFile;
    }
    @Override
    public void onPause(){
        super.onPause();
        // 보통 안쓰는 객체는 onDestroy에서 해제 되지만 카메라는 확실히 제거해주는게 안전하다.

    }



    public void setDirEmpty(String dirName) {
        I_count = 1;
        String path = Environment.getExternalStoragePublicDirectory(
                Environment.DIRECTORY_PICTURES).toString() + dirName;

        File dir = new File(path);
        File[] childFileList = dir.listFiles();

        for (File childFile : childFileList) {
            if (dir.exists())
                if (childFile.isDirectory()) {
                    setDirEmpty(childFile.getAbsolutePath()); //하위 디렉토리
                } else {
                    childFile.delete();//하위 파일
                }
        }
        dir.delete();
    }



}





