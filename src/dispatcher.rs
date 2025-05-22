use std::{collections::HashMap, fs, path::Path};
use serde::{Serialize, Deserialize};
use crate::scanner::Barcode;
use std::process::Command;

#[derive(Serialize, Deserialize, Debug)]
struct Action {
    description: String,
    command: String,
    args: Option<Vec<String>>,
    env: Option<HashMap<String, String>>,
}

#[derive(Serialize, Deserialize, Debug)]
struct Config {
    version: String,
    default: Option<Action>,
    mappings: HashMap<String, Action>,
}
pub struct Dispatcher {
    config: Config,
}

impl Dispatcher {
    pub fn new(config_path: &Path) -> Self {
        let config_str = fs::read_to_string(config_path).expect("Failed to read config file");
        let config: Config = serde_yml::from_str(&config_str).expect("Failed to parse config file");
        Dispatcher { config }
    }

    pub fn dispatch(&self, barcode: &Barcode) {
        if let Some(action) = self.config.mappings.get(&barcode.code) {
            self.execute_action(action);
        } else if let Some(default_action) = &self.config.default {
            self.execute_action(default_action);
        } else {
            eprintln!("No action found for barcode: {}", barcode.code);
        }
    }

    fn execute_action(&self, action: &Action) {
        println!("Executing action: {}", action.description);
        println!("Command: {}", action.command);
        if let Some(args) = &action.args {
            println!("Arguments: {:?}", args);
        }
        if let Some(env) = &action.env {
            println!("Environment variables: {:?}", env);
        }
        
        let mut cmd = Command::new(&action.command);
        if let Some(args) = &action.args {
            cmd.args(args);
        }
        if let Some(env) = &action.env {
            cmd.envs(env);
        }
        _ = cmd.spawn();
    }
}
