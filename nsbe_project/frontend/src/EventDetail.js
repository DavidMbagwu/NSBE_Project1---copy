import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Layout from './Layout';
import axios from 'axios';
import { Box, Grid, Paper, Stack, Typography, Button } from "@mui/material";
import CalendarMonthTwoToneIcon from '@mui/icons-material/CalendarMonthTwoTone';
import RoomTwoTone from '@mui/icons-material/RoomTwoTone';
import { handleRegister, handleUnregister } from './controllers/eventController';

function EventDetail() {
    const { slug } = useParams();
    const [event, setEvent] = useState(null);

    useEffect(() => {
        async function fetchEvent() {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/stage/event/${slug}`);
                setEvent(response.data);
            } catch (error) {
                console.log(error);
            }
        }

        fetchEvent();
    }, [slug]);

    if (!event) {
        return <div>Loading ... </div>;
    }

    const eventStartTime = new Date(event.start_time);
    const isUpcoming = eventStartTime > new Date();

    const handleButtonClick = async () => {
        if (!event.is_member_registed) {
            const result = await handleRegister(event.id);
            if (result.success) {
                setEvent({ ...event, is_member_registed: true });
                alert("Registered successfully");
            }
        } else {
            const result = await handleUnregister(event.id);
            if (result.success) {
                setEvent({ ...event, is_member_registed: false });
                alert("Unregistered successfully");
            }
        }
    };

    return (
        <Layout>
            <Box elevation={3} sx={{ padding: '16px', textAlign: 'left' }}>
                <Typography variant="h6">{event.title}</Typography>
                <Stack spacing={1} sx={{ marginY: '10px' }}>
                    <Stack alignItems="center" direction="row" gap={1}>
                        <CalendarMonthTwoToneIcon />
                        <Typography>{event.start_time} - {event.end_time}</Typography>
                    </Stack>
                    <Stack alignItems="center" direction="row" gap={1}>
                        <RoomTwoTone />
                        <Typography>{event.location}</Typography>
                    </Stack>
                </Stack>
                <Stack direction="row" spacing={2} sx={{ marginTop: '10px' }}>
                    {isUpcoming && (
                        <Button
                            variant="contained"
                            sx={{ backgroundColor: '#F5F5F7', color: '#201414' }}
                            onClick={handleButtonClick}
                        >
                            {event.is_member_registed ? 'Unregister' : 'Register'}
                        </Button>
                    )}
                </Stack>
            </Box>
            <Grid item xs={12} sm={6} md={4}>
                <Paper sx={{ padding: '16px' }}>
                    {event.description}
                </Paper>
            </Grid>
        </Layout>
    );
}

export default EventDetail;
