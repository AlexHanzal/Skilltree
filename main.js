const { app, BrowserWindow } = require('electron/main')
const { ipcMain } = require('electron');
const fs = require('fs');
const path = require('path');

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  })

  win.loadFile('../hmtl/index.html')
}

app.whenReady().then(() => {
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow()
    }
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

ipcMain.on('achievement-unlocked', (event, data) => {
  const dataFile = path.join(__dirname, '../data/data');
  let unlocked = [];
  try {
    if (fs.existsSync(dataFile)) {
      unlocked = JSON.parse(fs.readFileSync(dataFile, 'utf8'));
    }
  } catch (e) {
    unlocked = [];
  }
  if (!unlocked.includes(data.id)) {
    unlocked.push(data.id);
    fs.writeFileSync(dataFile, JSON.stringify(unlocked, null, 2), 'utf8');
  }
});

ipcMain.on('achievement-locked', (event, data) => {
  const dataFile = path.join(__dirname, '../data/data');
  let unlocked = [];
  try {
    if (fs.existsSync(dataFile)) {
      unlocked = JSON.parse(fs.readFileSync(dataFile, 'utf8'));
    }
  } catch (e) {
    unlocked = [];
  }
  // Remove the achievement if present
  const idx = unlocked.indexOf(data.id);
  if (idx !== -1) {
    unlocked.splice(idx, 1);
    fs.writeFileSync(dataFile, JSON.stringify(unlocked, null, 2), 'utf8');
  }
});

ipcMain.handle('get-unlocked-achievements', async () => {
  const dataFile = path.join(__dirname, '../data/data');
  let unlocked = [];
  try {
    if (fs.existsSync(dataFile)) {
      unlocked = JSON.parse(fs.readFileSync(dataFile, 'utf8'));
    }
  } catch (e) {
    unlocked = [];
  }
  return unlocked;
});