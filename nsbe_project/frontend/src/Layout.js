import React from 'react';
import { Link as RouterLink } from 'react-router-dom';
import { Box, List, ListItem, ListItemText, Stack } from '@mui/material';
import { Home, Folder, Star, CalendarToday, Person, ExitToApp, Help, Info } from '@mui/icons-material';
import './Layout.css'; 

// Import the logo image
import nsbe5g from './static/stage/logo/nsbe5g.png';

const Layout = ({ children }) => {
  return (
    <Box className="wrapper">
      <Box className="sidebar">
        <Box className="sidebar-header">
          <img src={nsbe5g} alt="mcneese_icon" />
        </Box>
        <List className="list">
          <ListItem>
            <RouterLink to="/" className="link">
              <Stack alignItems="center" direction="row" spacing={2}>
                <Home />
                <ListItemText primary="Home" />
              </Stack>
            </RouterLink>
          </ListItem>
          <ListItem>
            <RouterLink to="/directory" className="link">
              <Stack alignItems="center" direction="row" spacing={2}>
                <Folder />
                <ListItemText primary="Directory" />
              </Stack>
            </RouterLink>
          </ListItem>
          <ListItem>
            <RouterLink to="/points" className="link">
              <Stack alignItems="center" direction="row" spacing={2}>
                <Star />
                <ListItemText primary="Points" />
              </Stack>
            </RouterLink>
          </ListItem>
          <ListItem>
            <RouterLink to="/events" className="link">
              <Stack alignItems="center" direction="row" spacing={2}>
                <CalendarToday />
                <ListItemText primary="Events" />
              </Stack>
            </RouterLink>
          </ListItem>
          <ListItem>
            <RouterLink to="/profile" className="link">
              <Stack alignItems="center" direction="row" spacing={2}>
                <Person />
                <ListItemText primary="Profile" />
              </Stack>
            </RouterLink>
          </ListItem>
        </List>
        <List className="bottom_list">
          <ListItem>
            <RouterLink to="/logout" className="link">
              <Stack alignItems="center" direction="row" spacing={2}>
                <ExitToApp />
                <ListItemText primary="Log Out" />
              </Stack>
            </RouterLink>
          </ListItem>
          <ListItem>
            <RouterLink to="/help" className="link">
              <Stack alignItems="center" direction="row" spacing={2}>
                <Help />
                <ListItemText primary="Help" />
              </Stack>
            </RouterLink>
          </ListItem>
          <ListItem>
            <RouterLink to="/about" className="link">
              <Stack alignItems="center" direction="row" spacing={2}>
                <Info />
                <ListItemText primary="About" />
              </Stack>
            </RouterLink>
          </ListItem>
        </List>
      </Box>
      <Box className="content">
        {children}
      </Box>
    </Box>
  );
};

export default Layout;
