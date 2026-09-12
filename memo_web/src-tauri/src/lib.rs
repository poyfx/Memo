
use tauri::menu::{Menu, MenuItem};
use tauri::tray::{MouseButton, MouseButtonState, TrayIconBuilder, TrayIconEvent};
use tauri::{Manager, WebviewUrl, WebviewWindowBuilder};

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
  tauri::Builder::default()
    .plugin(tauri_plugin_notification::init())
    .invoke_handler(tauri::generate_handler![open_main_window])
    .setup(|app| {
        create_ball_window(app.handle())?;
        let open_item = MenuItem::with_id(app, "open", "打开", true, None::<&str>)?;
        let quit_item = MenuItem::with_id(app, "quit", "退出", true, None::<&str>)?;
        let menu = Menu::with_items(app, &[&open_item, &quit_item])?;
        TrayIconBuilder::new()
            .icon(app.default_window_icon().unwrap().clone())
            .menu(&menu)  
            .on_menu_event(|app, event| match event.id.as_ref() {
                "open" => show_main_window(app),
                "quit" => app.exit(0),
                _ => {}
            })
            .on_tray_icon_event(|tray, event| {
                if let TrayIconEvent::Click {
                    button: MouseButton::Left,
                    button_state: MouseButtonState::Up,
                    ..
                    } = event
                    {
                        show_main_window(tray.app_handle());
                    }
            })
            .build(app)?;

        if cfg!(debug_assertions) {
           app.handle().plugin(
           tauri_plugin_log::Builder::default()
           .level(log::LevelFilter::Info)
            .build(),
            )?;
            }   
            Ok(())
        })
        .on_window_event(|window, event| {
            if window.label() != "main" {
                return;
            }
            if let tauri::WindowEvent::CloseRequested { api,..} = event {
                api.prevent_close();

                let app = window.app_handle();
                let _ = window.hide();

                if let Some(ball) = app.get_webview_window("ball"){
                    let _ = ball.show();
                    let _ = ball.set_focus();
                }
            }
        })
            .run(tauri::generate_context!())
            .expect("error while running tauri application");                    
      
}

  fn show_main_window(app: &tauri::AppHandle) {
  if let Some(window) = app.get_webview_window("main") {
    let _ = window.unminimize();
    let _ = window.show();
    let _ = window.set_focus();
  }
   if let Some(ball) = app.get_webview_window("ball") {
    let _ = ball.hide();
  }
}

#[tauri::command]
fn open_main_window(app: tauri::AppHandle) -> Result<(), String> {
  show_main_window(&app);
  Ok(())
}

fn create_ball_window(app: &tauri::AppHandle) -> tauri::Result<()> {
  if app.get_webview_window("ball").is_some() {
    return Ok(());
  }

  let ball = WebviewWindowBuilder::new(app, "ball", WebviewUrl::App("index.html#/ball".into()))
    .title("悬浮球")
    .inner_size(56.0, 56.0)
    .decorations(false)
    .transparent(true)
    .shadow(false)
    .resizable(false)
    .skip_taskbar(true)
    .always_on_top(true)
    .build()?;

    let _ = ball.hide();
  Ok(())
}