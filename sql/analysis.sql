
-- Equipment Failure Prediction
-- SQL Data Analysis

-- 1. View all records
SELECT *
FROM equipment;

-- 2. Count total records
SELECT COUNT(*) AS total_records
FROM equipment;

-- 3. Check machine failure distribution
SELECT
    "Machine failure",
    COUNT(*) AS total_machines
FROM equipment
GROUP BY "Machine failure";

-- 4. Count machines by machine type
SELECT
    Type,
    COUNT(*) AS total_machines
FROM equipment
GROUP BY Type;

-- 5. Calculate average sensor readings
SELECT
    AVG("Air temperature [K]") AS avg_air_temperature,
    AVG("Process temperature [K]") AS avg_process_temperature,
    AVG("Rotational speed [rpm]") AS avg_rotational_speed,
    AVG("Torque [Nm]") AS avg_torque,
    AVG("Tool wear [min]") AS avg_tool_wear
FROM equipment;

-- 6. Machine failures by machine type
SELECT
    Type,
    COUNT(*) AS failure_count
FROM equipment
WHERE "Machine failure" = 1
GROUP BY Type
ORDER BY failure_count DESC;

-- 7. Average torque for failed and non-failed machines
SELECT
    "Machine failure",
    AVG("Torque [Nm]") AS average_torque
FROM equipment
GROUP BY "Machine failure";

-- 8. Average tool wear for failed and non-failed machines
SELECT
    "Machine failure",
    AVG("Tool wear [min]") AS average_tool_wear
FROM equipment
GROUP BY "Machine failure";

-- 9. Machines with high tool wear
SELECT *
FROM equipment
WHERE "Tool wear [min]" > 200
ORDER BY "Tool wear [min]" DESC;

-- 10. Failure count by machine type
SELECT
    Type,
    COUNT(*) AS total_records,
    SUM("Machine failure") AS failures
FROM equipment
GROUP BY Type
ORDER BY failures DESC;
