import kotlin.math.abs

fun main() {
    // 목표 채널
    val targetChannel = readln().toInt()
    // 목표 채널의 숫자 길이
    val targetChannelLength = targetChannel.toString().length
    // 고장난 버튼 수
    val destroyedNumberButtonsCount = readln().toInt()
    // 기본 채널
    val defaultChannel = 100

    if (defaultChannel == targetChannel) {
        println(0)
    } else if (destroyedNumberButtonsCount == 10) {
        println(abs(defaultChannel - targetChannel))
    } else if (destroyedNumberButtonsCount == 0) {
        println(minOf(targetChannelLength, abs(defaultChannel - targetChannel)))
    } else {
        val workingNumberButtons = 0.rangeTo(9).toSet().run {
            if (destroyedNumberButtonsCount > 0) {
                this - readln().split(" ").map { it.toInt() }.toSet()
            } else {
                this
            }
        }.sorted()

        // 숫자 버튼 클릭 만으로 목표 채널로 이동할 때의 클릭 횟수
        val pressCountOnlyWithChannelButtons = abs(defaultChannel - targetChannel)
        // 최소 횟수 갱신
        var minPressesCount = pressCountOnlyWithChannelButtons

        targetChannel.toString().map { it.toString().toInt() }.let { targetChannelNumbers ->
            if (targetChannelNumbers.all { it in workingNumberButtons }) {
                // 목표 채널로 즉시 이동가능 한 경우
                minPressesCount = minOf(targetChannelLength, minPressesCount)
            } else {
                // 숫자 버튼 클릭으로 이동가능한 모든 채널 목록 생성
                val allChannels = mutableListOf<Int>()
                workingNumberButtons.forEach {
                    if (it > 0) {
                        // 목표 채널 숫자 길이보다 하나 더 길게 채널 생성
                        workingNumberButtons.generateAllChannels(
                            it,
                            1,
                            (targetChannelLength + 1).coerceAtMost(6),
                            allChannels
                        )
                    } else {
                        allChannels.add(0)
                    }
                }

                // 모든 채널에 대하여 (채널 버튼 클릭 횟수 + 채널 변경 버튼 클릭 횟수) 연산 후 최소 횟수 갱신
                for (channel in allChannels) {
                    minPressesCount = minOf(channel.toString().length + abs(channel - targetChannel), minPressesCount)
                }
            }
        }

        println(minPressesCount)
    }
}


fun List<Int>.generateAllChannels(channel: Int, index: Int, maxIndex: Int, allChannels: MutableList<Int>) {
    if (index <= maxIndex) {
        allChannels.add(channel)

        for (num in this) {
            generateAllChannels(channel * 10 + num, index + 1, maxIndex, allChannels)
        }
    }
}
